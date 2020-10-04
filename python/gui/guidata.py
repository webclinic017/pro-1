# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # ウィンドウタイトルの設定
        master.title(u'物品検索')

        # ウィンドウの大きさの変更を規定
        master.resizable(width=False, height=False)

        # ウィンドウのグリッドを 1x1 にする
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -----物品検索フレーム-----------------------------
        # 物品検索ページフレーム作成
        self.frame_material = ttk.Frame(master, padding=16)

        self.frame_material.grid(row=0, column=0)

        self.frame_material.grid_propagate(0)

        # 検索フレーム
        self.frame_search = ttk.Frame(
            self.frame_material)
        self.frame_search.pack(expand=False, fill=tk.X)

        # 検索対象ラベル作成
        self.label1 = ttk.Label(self.frame_search, text='検索対象')
        self.label1.grid(row=0, column=0, sticky=tk.W)

        # 検索列設定コンボボックス作成
        # 項目作成
        self.types = (u'物品コード', u'カナ品名')

        # コンボボックスの変数作成
        self.combovalue = tk.StringVar()

        # コンボボックス作成
        self.combo1 = ttk.Combobox(
            self.frame_search, state='readonly', value=self.types,
            textvariable=self.combovalue
        )

        # 初期選択値設定
        self.combo1.current(0)

        self.combo1.grid(row=0, column=1)

        #
        self.label5 = ttk.Label(self.frame_search, text='検索ワード')
        self.label5.grid(row=1, column=0, pady=5)

        # 検索ワードエントリーの作成
        self.t = tk.StringVar
        self.entry1 = ttk.Entry(self.frame_search, textvariable=self.t)
        self.entry1.grid(row=1, column=1, pady=5)

        # 検索ボタン
        self.button1 = ttk.Button(
            self.frame_search,
            text=u'検索',
            command=lambda: self.get_keyword()
        )
        self.button1.grid(row=1, column=2, pady=5)

        # 表フレーム作成
        self.frame_table = ttk.Frame(self.frame_material)
        self.frame_table.pack(expand=False, fill=tk.X)

        # self.frame_table.pack_propagate(0)

        # 表の作成
        self.tree = ttk.Treeview(self.frame_table, height=20)

        # 列の定義
        self.tree['columns'] = (1, 2, 3, 4)
        self.tree['show'] = 'headings'
        self.tree.column(1, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(2, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(3, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(4, width=190, minwidth=190, stretch=tk.NO)

        # 見出しの定義
        self.tree.heading(1, text='index', anchor=tk.W)
        self.tree.heading(2, text='name', anchor=tk.W)
        self.tree.heading(3, text='num', anchor=tk.W)
        self.tree.heading(4, text='value', anchor=tk.W)

        # insert
        self.tree.insert('', "end", values=('1', 'apple', '2', '100'))
        self.tree.insert('', "end", values=('2', 'orange', '5', '120'))
        self.tree.insert('', "end", values=('3', 'grape', '1', '300'))
        self.tree.insert('', "end", values=('4', 'pineapple', '0', '200'))

        self.tree.pack(pady=10, side=tk.TOP, fill=tk.X)

        # スクロールバーの作成
        # 横方向
        '''
        self.hscrollbar = ttk.Scrollbar(self.tree, orient=tk.HORIZONTAL,
                                        command=self.tree.xview
                                        )
        self.tree.configure(xscrollcommand=lambda f,
                            l: self.hscrollbar.set(f, l))
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # 立て方向
        self.vscrollbar = ttk.Scrollbar(self.tree, orient=tk.VERTICAL,
                                        command=self.tree.yview
                                        )
        self.tree.configure(xscrollcommand=lambda f,
                            l: self.vscrollbar.set(f, l))
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        '''

        # --------------------------------------------------
        # -----組織検索フレーム------------------------------
        # 組織検索ページフレーム作成
        self.frame_organization = ttk.Frame(master, padding=16)

        self.frame_organization.grid(row=0, column=0, sticky='nsew')

        self.label2 = ttk.Label(self.frame_organization, text='組織検索画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label2.pack()

        self.button2 = ttk.Button(self.frame_organization, text='change',
                                  command=lambda: self.change_page(self.frame_material))

        self.button2.pack(side=tk.TOP)

        # --------------------------------------------------
        # -----連絡先検索フレーム----------------------------
        # 連絡先検索ページフレーム作成
        self.frame_contact = ttk.Frame(master, padding=16)

        self.frame_contact.grid(row=0, column=0, sticky='nsew')

        self.label3 = ttk.Label(self.frame_contact, text='連絡先検索画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label3.pack()

        # --------------------------------------------------
        # -----csvインポート検索フレーム---------------------
        # csvインポートページフレーム作成
        self.frame_import = ttk.Frame(master, padding=16)

        self.frame_import.grid(row=0, column=0, sticky='nsew')

        self.label4 = ttk.Label(self.frame_import, text='csvインポート画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label4.pack()

        # --------------------------------------------------

        # -----画面遷移ボタンの作成-------------------------
        # 画面下部バーの設定
        self.make_underbar(master)
        # -------------------------------------------------

        # frame_materialを一番上に表示
        self.frame_material.tkraise()

    def change_page(self, page):
        page.tkraise()

    def get_keyword(self):
        # キーワードを取得する
        print(self.combovalue.get())

    def make_underbar(self, frame_parent):
        # 下バー
        # ウィンドウ下部バーフレームの作成
        self.frame_bar = ttk.Frame(frame_parent, padding=10)
        self.frame_bar.grid(row=1, column=0)

        # キャンバスの作成
        self.canvas_under = tk.Canvas(
            self.frame_bar)
        self.canvas_under.pack(side=tk.BOTTOM, fill=tk.X)

        # 物品検索ボタンフレーム
        self.button_material = make_button(
            move_page=self.frame_material,
            canvas=self.canvas_under,
            image_path='./image/server.png',
            label_name='物品検索',
            order=3
        )

        # 組織検索ボタンフレーム
        self.button_organization = make_button(
            move_page=self.frame_organization,
            canvas=self.canvas_under,
            image_path='./image/location.png',
            label_name='組織検索',
            order=1
        )

        # 連絡先検索ボタンフレーム
        self.button_contact = make_button(
            move_page=self.frame_contact,
            canvas=self.canvas_under,
            image_path='./image/phone.png',
            label_name='連絡先検索',
            order=2
        )

        # csvインポートフレーム
        self.button_import = make_button(
            move_page=self.frame_import,
            canvas=self.canvas_under,
            image_path='./image/file.png',
            label_name='csvインポート',
            order=3
        )


class make_button(Application):
    def __init__(self, move_page, canvas, image_path, label_name, order):
        # イメージの作成
        image = Image.open(image_path)
        image = image.resize((50, 60))
        self.img = ImageTk.PhotoImage(image)

        self.frame_button = ttk.Frame(canvas, relief='flat')
        self.frame_button.pack(side=tk.LEFT, padx=60)

        # 遷移ボタン作成
        self.button_change = ttk.Button(
            self.frame_button,
            command=lambda: self.change_page(move_page),
            image=self.img
        )
        self.button_change.grid(row=0, column=order)

        # ラベル作成
        self.label_change = ttk.Label(
            self.frame_button, text=label_name
        )
        self.label_change.grid(row=1, column=order)


if __name__ == '__main__':
    # ルートウィンドウ要素の作成
    root = tk.Tk()

    # クラス呼び出し
    Application(master=root)

    root.mainloop()
