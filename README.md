# ESP-NOWでマルチホップ
ESP-NOWでマルチホップで通信するためのプログラムです．
詳しくは以下のリンクを参照して下さい
https://qiita.com/c0a21086/items/b97d6045244d901c46f6
## send.py
これはESP-NOWでデータを送信するためのプログラムです．
送信に使用するESP32にこのコードを実装してexecfile("send.py")で実行できます．
エラーが発生した場合はsend_error.logにエラーログを記録します．
実行結果は以下のように送信したデータの内容が表示されます．

![image](https://github.com/user-attachments/assets/5fe33726-c014-49e0-bb70-e21ae356c9ca)
## relay.py
これはESP-NOWで受信したデータを転送するためのプログラムです．
転送に使用するESP32にこのコードを実装してexecfile("relay.py")で実行できます．
エラーが発生した場合はrelay_error.logにエラーログを記録します．
実行結果は以下のように送信元のMACアドレスと転送したデータの内容が表示されます．

![image](https://github.com/user-attachments/assets/756c0a39-ecb7-4261-ab53-723bba8fbe53)
## receive.py
これはESP-NOWで送信されたデータを受信するためのプログラムです．
受信に使用するESP32にこのコードを実装してexecfile("receive.py")で実行できます．
エラーが発生した場合はreceive_error.logにエラーログを記録します．
実行結果は以下のように送信元のMACアドレスと受信したデータの内容が表示されます．

![image](https://github.com/user-attachments/assets/6d93cc72-7290-47f0-b24d-5a934118b13b)

