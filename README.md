# 席替え

一つのクラスにおいて、生徒の希望に応じて席替えを行うアプリケーションです。

### 機能

- 生徒全員が希望の席を指定
- 前席考慮

## 使い方

### `setting/sample.xlsx`を例に、設定ファイルを作成する

`setting/sample.xlsx`を参考にして、同様の設定ファイルを作成してください。
このファイルは以下で構成されています。

#### `members`シート
このシートには、各メンバー（生徒）の出席番号・名前・希望の席・前席考慮の有無についてのデータを記入します。
例えば以下のようなものです。

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-cly1">出席番号</th>
    <th class="tg-cly1">名前</th>
    <th class="tg-cly1">希望</th>
    <th class="tg-cly1">前席考慮</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cly1">number</td>
    <td class="tg-cly1">name</td>
    <td class="tg-cly1">hopes</td>
    <td class="tg-cly1">glasses</td>
  </tr>
  <tr>
    <td class="tg-cly1">1</td>
    <td class="tg-cly1">川野 洵子</td>
    <td class="tg-cly1">C2</td>
    <td class="tg-cly1">1</td>
  </tr>
  <tr>
    <td class="tg-cly1">2</td>
    <td class="tg-cly1">堀江 銀之助</td>
    <td class="tg-cly1">A3,A4</td>
    <td class="tg-cly1">0</td>
  </tr>
  <tr>
    <td class="tg-cly1">3</td>
    <td class="tg-cly1">浜田 大夢</td>
    <td class="tg-cly1">D6</td>
    <td class="tg-cly1">0</td>
  </tr>
  <tr>
    <td class="tg-cly1">4</td>
    <td class="tg-cly1">新谷 一智</td>
    <td class="tg-cly1">B3</td>
    <td class="tg-cly1">0</td>
  </tr>
</tbody>
</table>

- 出席番号  
出席番号を記入します。**必ず番号で記入してください。**

- 名前  
氏名を記入します。省略しても構いません。

- 希望  
座席の希望を指定します。座席の番号は`desks_map`シートと対応しています。
複数ある場合は、スペースなしカンマ区切りで入力してください。

- 前席考慮
視力等の理由で前にしなければならない人を指定します。前席考慮が必要な人は`1`、そうでない人を`0`とします。
前席指定は`glasses_desks`シートで行います。

2行目は左から順に `number, name, hopes, glasses`となっています。**この行は変更しないでください。**
変更した場合、うまく動きません。

#### `desks_map`シート
座席の位置と、上記hopesで用いる名前を指定します。例えば、以下のようなものです。

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-cly1"></th>
    <th class="tg-cly1">B1</th>
    <th class="tg-cly1">C1</th>
    <th class="tg-cly1">D1</th>
    <th class="tg-cly1">E1</th>
    <th class="tg-cly1">F1</th>
    <th class="tg-cly1"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cly1">A2</td>
    <td class="tg-cly1">B2</td>
    <td class="tg-cly1">C2</td>
    <td class="tg-cly1">D2</td>
    <td class="tg-cly1">E2</td>
    <td class="tg-cly1">F2</td>
    <td class="tg-cly1">G2</td>
  </tr>
  <tr>
    <td class="tg-cly1">A3</td>
    <td class="tg-cly1">B3</td>
    <td class="tg-cly1">C3</td>
    <td class="tg-cly1">D3</td>
    <td class="tg-cly1">E3</td>
    <td class="tg-cly1">F3</td>
    <td class="tg-cly1">G3</td>
  </tr>
  <tr>
    <td class="tg-cly1">A4</td>
    <td class="tg-cly1">B4</td>
    <td class="tg-cly1">C4</td>
    <td class="tg-cly1">D4</td>
    <td class="tg-cly1">E4</td>
    <td class="tg-cly1">F4</td>
    <td class="tg-cly1">G4</td>
  </tr>
  <tr>
    <td class="tg-cly1">A5</td>
    <td class="tg-cly1">B5</td>
    <td class="tg-cly1">C5</td>
    <td class="tg-cly1">D5</td>
    <td class="tg-cly1">E5</td>
    <td class="tg-cly1">F5</td>
    <td class="tg-cly1">G5</td>
  </tr>
  <tr>
    <td class="tg-cly1">A6</td>
    <td class="tg-cly1">B6</td>
    <td class="tg-cly1">C6</td>
    <td class="tg-cly1">D6</td>
    <td class="tg-cly1">E6</td>
    <td class="tg-cly1">F6</td>
    <td class="tg-cly1">G6</td>
  </tr>
  <tr>
    <td class="tg-cly1">A7</td>
    <td class="tg-cly1">B7</td>
    <td class="tg-cly1">C7</td>
    <td class="tg-cly1">D7</td>
    <td class="tg-cly1">E7</td>
    <td class="tg-cly1">F7</td>
    <td class="tg-cly1">G7</td>
  </tr>
</tbody>
</table>

## Q&A



## 応用
このアプリケーションは、うまく活用すれば以下のような使用も可能です。
- シフトの作成
