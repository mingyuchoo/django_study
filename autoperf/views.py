import yaml
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from autoperf.harry import generate_test_plan
from autoperf.harpy.har import Har


def index(request):
    context = {}
    if request.method == 'POST' and request.FILES['source_file']:
        source_file = request.FILES['source_file']
        fs = FileSystemStorage()
        filename = fs.save(source_file.name, source_file)
        new_path = ''.join([settings.MEDIA_ROOT, '/', filename])
        har_file = Har(new_path)
        jmx_file_name = ''.join([filename, '.jmx'])
        jmx_file = generate_test_plan(har_file, output=jmx_file_name)
        response = HttpResponse(jmx_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % jmx_file_name
        return response
    else:
        pass
    return render(request, 'autoperf/index.html', context)


def json_string(request):
    import json
    context = {}
    if request.method == 'POST':
        source = request.POST['source']
        # print('>>>>', json.dumps(source))
        context = {'converted_data': json.dumps(source)}
    else:
        pass
    return render(request, 'autoperf/json_string.html', context)


def yaml_string(request):
    context = {}
    template_json = {
      "included-configs": [
      "./base_config.yaml"
      ],
      "execution": [
        {
          "concurrency": 1,
          "ramp-up": "1m",
          "hold-for": "5m",
          "iterations": 20,
          "write-xml-jtl": "full",
          "scenario": "ThreadGroup01"
        }
      ],
      "scenarios": {
        "ThreadGroup01": {
          "retrieve-resources": "false",
            "think-time": "0s10000ms",
            "data-sources": [
              {
                "path": "test_data_01.csv",
                "loop": "true"
              }
            ],
          "headers": {},
          "requests": [
            {
              "once": [
                {
                  "include-scenario": "ucube_login"
                }
              ]
            },
            {
              "transaction": "tc_01",
              "include-timers": "false",
              "do": [
              ]
            }
          ],
          "store-cache": "false",
          "store-cookie": "true",
          "use-dns-cache-mgr": "false"
        }
      }
    }
    method = url = version = ""
    if request.method == 'POST':
        source = request.POST['source']
        header = source.split('\r\n\r\n')[0]
        body = source.split('\r\n\r\n')[1]

        # HEADER
        req = {
          "follow-redirects": "true",
          "label": "",
          "url": "",
          "method": "",
          "body": "",
          "assert": [
            {
              "contains": [
                "SUCC"
              ]
            }
          ]
        }
        for index, item in enumerate(header.splitlines()):
            try:
                if ': ' in item:
                    key, value = item.split(': ')
                    template_json['scenarios']['ThreadGroup01']['headers'][key] = value
                else:
                    if 'GET' in item:
                        method, url, version = item.split(' ')
                    elif 'POST' in item:
                        method, url, version = item.split(' ')
                        # BODY
                        req['body'] = json.dumps(body)
                        print('body>>> ', req['body'])
                    else:
                        pass
                    req['label'] = '/'.join(url.split('/')[3:])
                    req['url'] = url
                    req['method'] = method
            except ValueError as e:
                print('>>> ValueError')

        template_json['scenarios']['ThreadGroup01']['requests'][1]['do'].append(req)
        print('>>>>>', yaml.dump(template_json))
        context = {'data': yaml.dump(template_json).replace("!!python/unicode", "")}
    else:
        pass
    return render(request, 'autoperf/yaml_string.html', context)

