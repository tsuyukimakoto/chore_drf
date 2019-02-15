# Chore Django REST framework

[![travis](https://travis-ci.com/tsuyukimakoto/chore_drf.svg?branch=master)](https://travis-ci.com/tsuyukimakoto/chore_drf) [![codecov](https://codecov.io/gh/tsuyukimakoto/chore_drf/branch/master/graph/badge.svg)](https://codecov.io/gh/tsuyukimakoto/chore_drf) [![Updates](https://pyup.io/repos/github/tsuyukimakoto/chore_drf/shield.svg)](https://pyup.io/repos/github/tsuyukimakoto/chore_drf/) [![Python 3](https://pyup.io/repos/github/tsuyukimakoto/chore_drf/python-3-shield.svg)](https://pyup.io/repos/github/tsuyukimakoto/chore_drf/)

Django
-----------------------------------

https://www.djangoproject.com

Django makes it easier to build better Web apps more quickly and with less code.

PythonでWebアプリケーションを作る場合はDjangoを使っておくと良いです。
油断して軽量級を使うと結局…ということになりかねません。
よくわかっていて特定のものを選ぶ場合にはその限りではありません。

Django REST Framework
-----------------------------------

https://www.django-rest-framework.org

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Djangoを使ってWeb APIを作るときに便利なフレームワークです。
超ベーシックなものはコード量少なく書けるはず。

Django-environ
-----------------------------------

https://django-environ.readthedocs.io/en/latest/

Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application.

環境によって違う設定を環境変数を使ってDjangoの設定に渡したいときに便利です。
環境変数がない場合にはファイルから参照できたりするので、ローカルはファイルからなどとやりやすい。

flake8
-----------------------------------

http://flake8.pycqa.org/en/latest/

Your Tool For Style Guide Enforcement

コードの書き方をチェックするツール。
長さ制限やimport順など、統一された書き方を矯正できる。

pytest
-----------------------------------

https://pytest.org

小回りの効くテストランナー。
pytest-djangoなどプラグインが豊富らしい。
エラー個所についても違いがわかりやすくアウトプットされる。

tox
-----------------------------------

https://tox.readthedocs.io/en/latest/

tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.

複数のランタイムバージョンなど、環境違いのテストを走らせるられる。

Travis CI
-----------------------------------

https://travis-ci.com

Travis CI supports your development process by automatically building and testing code changes, providing immediate feedback on the success of the change.

CIサービス。GitHubと連携して自動でテストを実行できる。

Codecov
-----------------------------------

https://codecov.io

Codecov provides highly integrated tools to group, merge, archive, and compare coverage reports.

カバレッジレポート。PRにカバレッジレポートを埋め込んでくれる。
