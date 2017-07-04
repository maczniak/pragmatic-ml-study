[숙제][homework_description]로 만든, 감정 분석 Slack 봇입니다.
 [Google Cloud Natural Langage API][google_cloud_natural_language_api]로 감정
 분석을 하고, 봇 플랫폼 대신 [python-rtmbot][python_rtmbot] 라이브러리를
 사용하였습니다. 사용하려면, `rtmbot.conf` 파일에 봇 사용자의 OAuth access
 token을 입력한 후 `rtmbot` 명령어를 실행합니다.

```
$ pip3 install -r requirements.txt
$ gcloud auth application-default login # Google Cloud authentication
$ cp rtmbot.conf.sample rtmbot.conf # and edit rtmbot.conf
$ rtmbot
```

## TODO

* disable Slack message echoes
* make rtmbot error messages more friendly
* try bot platforms
* read Slack API documents

[homework_description]: https://www.facebook.com/groups/634363263421303/permalink/657682621089367/
[google_cloud_natural_language_api]: https://cloud.google.com/natural-language/
[python_rtmbot]: https://github.com/slackapi/python-rtmbot

