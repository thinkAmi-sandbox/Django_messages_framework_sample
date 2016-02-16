# Django_messages_framework_sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_messages_framework_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver


# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)

# 未入力時に、エラーのフラッシュメッセージを表示
>start http://localhost:8000/mysite/error-flash

# フラッシュメッセージを削除(成功してもフラッシュメッセージなし)
>start http://localhost:8000/mysite/remove-flash
# フラッシュメッセージを削除しない(成功したらフラッシュメッセージを表示)
>start http://localhost:8000/mysite/remove-flash/?a=1

# イテレータを回してもフラッシュメッセージを表示する
>start http://localhost:8000/mysite/reuse-flash

# SuccessMessageMixinを使った、成功時のフラッシュメッセージ表示
>start http://localhost:8000/mysite/mixin-flash
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.2

　  
## 関係するブログ

[Djangoで、messages frameworkを使ったフラッシュメッセージを試してみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/02/17/060852)