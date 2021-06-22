#第16章　チャレンジ問題
#No.1_BashでSelf-taugthと出力しよう。

echo "Self-taugth"

#No.2_ホームディレクトリ以外のパスから、ホームディレクトリに現在の作業ディレクトリを移動しよう。
#     パスは絶対パスと相対パスの両方で実行しよう。

cd /home/fxrun221
cd ../fxrun221

#No.3_環境変数$python_projectsを作って、あなたがPythonのファイルを置いているディレクトリの絶対パスを設定しよう。
#     環境変数を.profileファイルに保存して、cd $python_projectsコマンドでそのディレクトリに移動しよう。

python_projects=/home/fxrun/python/py
export python_projects
cd $python_projects
