# jui-app-server

jui.io 앱에서 쓰는 정적 데이터 파일을 서빙하고, 레거시 `export.php`의 강제 다운로드 동작을 대체하는 Flask 서버입니다.

## 배포 주소

https://feisty-rigging-490112-v2.appspot.com

Google App Engine (`asia-northeast3`, 서울 리전)에 배포되어 있습니다.

## 엔드포인트

- `GET /<파일경로>` : 디렉터리 내 정적 파일(`menu_ui.json`, `menu_chart.json`, `facebookgroup_data/*` 등)을 그대로 서빙합니다. 서버 구현 파일(`app.py`, `app.yaml`, `requirements.txt`, `.gcloudignore`, `venv/`, `.git`)은 서빙 대상에서 제외됩니다.
- `POST /export` : `filename`, `filetext` 폼 파라미터를 받아 강제 다운로드 헤더(`Content-Disposition: attachment` 등)와 함께 그대로 응답합니다. 원본 `export.php`와 동일한 동작입니다.

## 로컬 실행

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python app.py
```

`http://localhost:5000`에서 확인할 수 있습니다.

## 배포

```bash
gcloud app deploy --project=feisty-rigging-490112-v2
```
