# 席替え

![test](https://github.com/mo-mo-666/seat-change-for-class/workflows/test/badge.svg)

一つのクラスにおいて、生徒の希望に応じて席替えを行うアプリケーションです。

## 機能

- 生徒全員が希望の席を指定
- 前席考慮

## 使い方

### 設定ファイルを作成する

`setting/sample.xlsx`の例を参考にして、同様の設定ファイルを作成してください。
このファイルは以下で構成されています。

#### `members`シート
このシートには、各メンバー（生徒）の出席番号・名前・希望の席・前席考慮の有無についてのデータを記入します。
例えば以下のようなものです。

```text
+----------+-------------+-------+----------+
| 出席番号 | 名前        | 希望  | 前席考慮 |
+----------+-------------+-------+----------+
| number   | name        | hopes | glasses  |
+----------+-------------+-------+----------+
| 1        | 川野 洵子   | C2    | 1        |
+----------+-------------+-------+----------+
| 2        | 堀江 銀之助 | A3,A4 | 0        |
+----------+-------------+-------+----------+
| 3        | 浜田 大夢   | D6    | 0        |
+----------+-------------+-------+----------+
| 4        | 新谷 一智   | B3    | 0        |
+----------+-------------+-------+----------+
```

- 出席番号  
出席番号を記入します。**必ず数字で記入してください。**

- 名前  
氏名を記入します。空白でも構いません。

- 希望  
座席の希望を指定します。座席の名称は`desks_map`シートで定義したものを記入してください。
希望が複数ある場合は、スペースなしカンマ区切りで入力してください。

- 前席考慮
視力等の理由で前にしなければならない人を指定します。前席考慮が必要な人は`1`、そうでない人を`0`と入力してください。
前席指定は`glasses_desks`シートで行います。

2行目は左から順に `number, name, hopes, glasses`となっています。**この行は変更しないでください。**
変更した場合、うまく動きません。

#### `desks_map`シート
座席の位置と、上記hopesで用いる名前を指定します。例えば、以下のようなものです。

```text
+----+----+----+----+----+----+----+
|    | B1 | C1 | D1 | E1 | F1 |    |
+----+----+----+----+----+----+----+
| A2 | B2 | C2 | D2 | E2 | F2 | G2 |
+----+----+----+----+----+----+----+
| A3 | B3 | C3 | D3 | E3 | F3 | G3 |
+----+----+----+----+----+----+----+
| A4 | B4 | C4 | D4 | E4 | F4 | G4 |
+----+----+----+----+----+----+----+
| A5 | B5 | C5 | D5 | E5 | F5 | G5 |
+----+----+----+----+----+----+----+
| A6 | B6 | C6 | D6 | E6 | F6 | G6 |
+----+----+----+----+----+----+----+
| A7 | B7 | C7 | D7 | E7 | F7 | G7 |
+----+----+----+----+----+----+----+
```

座席を置きたい位置に一意の名前を定義してください。

#### `glasses_desks`シート
前席考慮の際の座席を指定します。例えば、以下のようなものです。

```text
+--+--+----+----+----+--+--+
|  |  | C1 | D1 | E1 |  |  |
+--+--+----+----+----+--+--+
|  |  | C2 | D2 | E2 |  |  |
+--+--+----+----+----+--+--+
|  |  | C3 | D3 | E3 |  |  |
+--+--+----+----+----+--+--+
|  |  |    |    |    |  |  |
+--+--+----+----+----+--+--+
|  |  |    |    |    |  |  |
+--+--+----+----+----+--+--+
|  |  |    |    |    |  |  |
+--+--+----+----+----+--+--+
|  |  |    |    |    |  |  |
+--+--+----+----+----+--+--+
```

前席考慮必要人数より、前席指定座席の数が多くなるようにしてください。

#### 注意
各シートは**書式なし**で記入してください。
Excelファイルのフォントを変えたり、枠線を付けたりすると、うまく動作しません。  
書式をクリアするには、`すべてのセルを選択 -> ホームタブ -> クリア -> 書式のクリア`
の手順を辿ってください。


### 実行する
設定ファイルを適切な位置に置き、`seat_changer.py`を実行します。

```bash
python seat_changer.py
```

あるいは`seat_changer.exe`を持っている場合は、ダブルクリックまたはコマンドプロンプトから`seat_changer.exe`と実行してください(Windows)。

設定ファイルのパスを指定するように求められるので、入力してください。
実行は数秒～数十秒で終わります。

## 出力
出力は、指定した設定ファイルの新しいワークシートに記入されます。例えば、以下のようなものです。  
具体的には`setting/result_sample.xlsx`を参照してください。

#### `result_members`シート
`members`シートに、座席結果を追加した形で出力します。

```text
+--------+-------------+-------+---------+-----------+
|        |             |       |         |           |
+--------+-------------+-------+---------+-----------+
| number | name        | hopes | glasses | mem_place |
+--------+-------------+-------+---------+-----------+
| 1      | 川野 洵子   | C2    | 1       | C2        |
+--------+-------------+-------+---------+-----------+
| 2      | 堀江 銀之助 | A3,A4 | 0       | A5        |
+--------+-------------+-------+---------+-----------+
| 3      | 浜田 大夢   | D6    | 0       | D7        |
+--------+-------------+-------+---------+-----------+
| 4      | 新谷 一智   | B3    | 0       | B3        |
+--------+-------------+-------+---------+-----------+
```

`mem_place`列が座席結果です。  
1行目が空白なのは仕様です。

#### `result_num_map`シート
座席結果を出席番号であらわしたものです。

```text
+----+----+----+----+----+----+----+
|    | 19 | 10 | 23 | 24 | 44 |    |
+----+----+----+----+----+----+----+
| 26 | 11 | 1  | 43 | 36 | 45 | 7  |
+----+----+----+----+----+----+----+
| 12 | 4  | 39 | 17 | 32 | 31 | 14 |
+----+----+----+----+----+----+----+
| 27 | 41 | 46 | 33 | 30 | 42 | 47 |
+----+----+----+----+----+----+----+
| 2  | 18 | 40 | 34 | 16 | 37 | 13 |
+----+----+----+----+----+----+----+
| 5  | 22 | 20 | 35 | 38 | 28 | 8  |
+----+----+----+----+----+----+----+
| 6  | 21 | 25 | 3  | 9  | 29 | 15 |
+----+----+----+----+----+----+----+
```

#### `result_name_map`シート
座席結果を名前であらわしたものです。

```text
+-------------+-------------+-----------+-----------+-------------+---------------------------+
|            | 武藤 順子   | 宮内 彰揮 | 深沢 則重 | 村井 準一郎 | 村井 佐十郎 |           |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 塚本 研五   | 高島 理絵   | 川野 洵子 | 若林 亜依 | 野沢 邦江   | 田上 孝成   | 松浦 健也   |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 杉本 真知子 | 新谷 一智   | 工藤 宏幸 | 高橋 洋和 | 長沢 克     | 久保 多栄子 | 森山 美貴   |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 石田 美津江 | 清水 征二郎 | 藤沢 利克 | 阿部 里香 | 荻野 惣之助 | 長野 菊治   | 藤村 英則   |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 堀江 銀之助 | 滝沢 準一郎 | 新田 俊憲 | 寺田 保平 | 福井 和広   | 高松 有     | 阿部 十三男 |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 杉浦 美次   | 大西 竹義   | 吉田 久紀 | 茂木 信好 | 藤田 利克   | 中沢 元臣   | 樋口 繁美   |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
| 池田 秀一   | 小山 好利   | 中谷 雅栄 | 浜田 大夢 | 中尾 秋代   | 広瀬 正輝   | 田口 直武   |
+-------------+-------------+-----------+-----------+-------------+-------------+-------------+
```

#### `result_loss`シート
希望の座席と実際の座席が"どのくらい離れているか"をあらわす指標です。
この数値があまりにも大きい場合（10000以上）、前席考慮がうまくいっていないので、
確認し、実行し直してください。  
数回やってもうまくいかない場合は、前席考慮希望者よりも前席指定座席が少ない可能性があります。
その場合は、前席指定座席を増やしてください。


## うまく実行されないときは
うまく実行されないときは、以下を確認してください。

- ワークシートの名前が間違っていないか  
ワークシートの名前が間違っている場合、うまく実行されません。
`members, desks_map, glasses_desks`が正しい名前です。

- 設定ファイルで、フォント・文字サイズ・文字色の変更やセルに枠線をつける等していないか  
設定ファイルは記入のみ行い、フォントなど書式を変更しないでください。
`すべてのセルを選択 -> ホームタブ -> クリア -> 書式のクリア`
で書式の削除が可能です。

- 設定ファイルで、各セルに余計なスペースが入っていないか  
設定ファイルを読み取る際、スペースも文字として認識されます。特に座席希望や座席配置を記入する際、
末尾、あるいはカンマ区切りの途中でスペースが入っていないかや、空白のセルに
余計なスペースがないかを確認してください。

- 設定ファイルで、`members`シートの2行目を変更していないか  
`members`シートの2行目を変更した場合、うまく実行されません。左から順に
`number, name, hopes, glasses`としてください。

- 生徒数と座席の数が一致しているか  
`members`シートで記入した生徒数と`desks_map`シートでの座席数は同数でなければなりません。

- 実行の際、設定ファイルがないといわれてしまう  
設定ファイルはカレントディレクトリからの相対パスで指定してください。`seat_changer.exe`をダブルクリックで
実行した場合は、`seat_changer.exe`があるディレクトリ（フォルダ）からの相対パスで指定してください。
また設定ファイルを指定する際は、拡張子を省略することなく、`.xlsx`まで入力してください。

- それでもうまく実行されない  
`seat_changer.exe`で実行している場合は、コマンドプロンプトで実行すればエラーを確認できます。
可能であれば、エラーを確認してください。そうでない場合も、設定ファイルを送って頂ければ対応いたします。


## 応用
このアプリケーションは、うまく活用すれば以下のような使用も可能です。
- シフトの作成

## ライセンス
MIT  
……加筆・書き換え・再配布・商用利用など無制限に利用可能。
ただし、作者または著作権者は、ソフトウェアに関してなんら責任を負わない。
