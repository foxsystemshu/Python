import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import json
# print(json.dumps(["Item", 4, {"key": "value"}], sort_keys=True, indent=4))


class Interface:
    def __init__(self, title, x_size, y_size, interface_window, data, canvas):
        self.ssv = None
        self.rsv = None
        self.sv = None
        self.id = None
        self.resultsText = None
        self.lbl_results_txt = None
        self.btn_next = None
        self.btn_search = None
        self.btn_previous = None
        self.txt_s_identifier = None
        self.txt_c_results = None
        self.txt_c_identifier = None
        self.lbl_s_identifier = None
        self.lbl_c_results = None
        self.lbl_results_ch = None
        self.lbl_results = None
        self.lbl_c_identifier = None
        self.lbl_identifier_ch = None
        self.lbl_identifier_txt = None
        self.lbl_identifier = None
        self.window = interface_window
        self.window.title(title)
        self.window.minsize(x_size, y_size)
        self.window.maxsize(x_size, y_size)

        self.__set_obj()
        self.data_dic = data
        self.current_data_view = 0
        self.results = self.__results_to_str(self.data_dic[self.current_data_view]["results"])
        self.id = self.data_dic[self.current_data_view]["identifier"]
        self.__set_labels(self.id, self.results)

        self.results_img = self.data_dic[self.current_data_view]["result_image"]
        self.id_img = self.data_dic[self.current_data_view]["identifier_image"]
        self.canvas = canvas

        self.__set_img(self.id_img, self.results_img)

    def __set_obj(self):
        # fixed label objects

        self.lbl_identifier = tk.Label(self.window, text="Identifier:")
        self.lbl_identifier.place(relx=0.08, rely=0.08)

        self.lbl_c_identifier = tk.Label(self.window, text="Confirmed identifier:")
        self.lbl_c_identifier.place(relx=0.08, rely=0.12)

        self.lbl_results = tk.Label(self.window, text="Results:")
        self.lbl_results.place(relx=0.08, rely=0.25)

        self.lbl_c_results = tk.Label(self.window, text="Confirmed results:")
        self.lbl_c_results.place(relx=0.08, rely=0.29)

        self.lbl_s_identifier = tk.Label(self.window, text="Identifier:")
        self.lbl_s_identifier.place(relx=0.40, rely=0.78)

        # Input objects
        self.sv = tk.StringVar(name="identifier")
        self.sv.trace_add(
            "write",
            self.__identifier_change_handler
        )

        self.txt_c_identifier = tk.Entry(self.window, width=20, textvariable=self.sv)
        self.txt_c_identifier.place(relx=0.25, rely=0.12)

        self.rsv = tk.StringVar(name="results")
        self.rsv.trace_add(
            "write",
            self.__results_change_handler
        )

        self.txt_c_results = tk.Entry(self.window, width=20, textvariable=self.rsv)
        self.txt_c_results.place(relx=0.25, rely=0.29)

        self.txt_s_identifier = tk.Entry(self.window, width=20)
        self.txt_s_identifier.place(relx=0.48, rely=0.78)

        # Button objects
        self.btn_previous = tk.Button(self.window, command=self.__show_previous)
        self.btn_previous["text"] = "Show previous"
        self.btn_previous.place(relx=0.08, rely=0.85)

        self.btn_search = tk.Button(self.window, command=self.__search_msg)
        self.btn_search["text"] = "Search"
        self.btn_search.place(relx=0.492, rely=0.85)

        self.btn_next = tk.Button(self.window, command=self.__show_next)
        self.btn_next["text"] = "Show next"
        self.btn_next.place(relx=0.85, rely=0.85)

        self.lbl_results_ch = tk.Label(self.window, textvariable=self.lbl_results_txt)
        self.lbl_results_ch.place(relx=0.25, rely=0.25)

        self.lbl_identifier_ch = tk.Label(self.window, textvariable=self.lbl_identifier_txt)
        self.lbl_identifier_ch.place(relx=0.25, rely=0.08)

    def __set_labels(self, idText, resultsText):
        self.id = idText
        self.resultsText = resultsText
        self.lbl_identifier_ch.config(text=idText)
        self.lbl_results_ch.config(text=resultsText)
        self.txt_c_identifier.configure(state='normal')
        self.txt_c_identifier.delete(0, 'end')
        self.txt_c_results.configure(state='normal')
        self.txt_c_results.delete(0, 'end')

    def __set_img(self, id_img, results_img):
        self.canvas.set_img(id_img, results_img)

    def __results_to_str(self, results):
        tmp_str = ""
        for x in results:
            tmp_str += str(x) + ","

        return tmp_str[:-1]

    def __identifier_change_handler(self, name, index, operation):
        self.__check_identifier()

    def __check_identifier(self):
        c_id = self.data_dic[self.current_data_view]["confirmed_identifier"]
        if c_id == "":
            if self.sv.get() == self.id:
                self.txt_c_identifier.configure(state='disabled')
                return True
            else:
                print("rossz")
        else:
            if self.sv.get() == c_id:
                self.txt_c_identifier.configure(state='disabled')
                return True
            else:
                print("rossz")

    def __results_change_handler(self, name, index, operation):
        self.__check_results()

    def __check_results(self):
        cc_r = self.__results_to_str(self.data_dic[self.current_data_view]["confirmed_results"])

        if cc_r == "":
            if str(self.rsv.get()) == self.results:
                self.txt_c_results.configure(state='disabled')
                return True
            else:
                print("Rossz")
        else:
            if str(self.rsv.get()) == cc_r:
                self.txt_c_results.configure(state='disabled')
                return True
            else:
                print("Rossz")

    def __show_next(self):
        if self.current_data_view < len(self.data_dic) - 1:
            self.current_data_view = self.current_data_view + 1

        self.__set_labels(self.data_dic[self.current_data_view]["identifier"],
                          self.__results_to_str(self.data_dic[self.current_data_view]["results"]))

        self.__set_img(self.data_dic[self.current_data_view]["identifier_image"],
                       self.data_dic[self.current_data_view]["result_image"])

    def __show_previous(self):
        if len(self.data_dic) - 1 >= self.current_data_view > 0:
            self.current_data_view = self.current_data_view - 1

        self.__set_labels(self.data_dic[self.current_data_view]["identifier"],
                          self.__results_to_str(self.data_dic[self.current_data_view]["results"]))
        self.__set_img(self.data_dic[self.current_data_view]["identifier_image"],
                       self.data_dic[self.current_data_view]["result_image"])

    def __search_msg(self):
        if not self.__search_id():
            msg = "Nem találtunk ilyet: " + self.txt_s_identifier.get()
            messagebox.showinfo("Információ", msg)

            print("Nem találtunk ilyet: ", self.txt_s_identifier.get())

    def __search_id(self):
        for data in self.data_dic:
            if data["identifier"] == self.txt_s_identifier.get():
                self.__set_labels(data["identifier"], data["results"])
                return True

    def start(self):
        self.window.mainloop()


class Data:
    @staticmethod
    def read_data(path):
        with open(path) as json_file:
            data = json.load(json_file)
        return data


class ImageObj:
    def __init__(self, win):
        self.w = win

    def set_img(self, path1, path2):
        canvas1 = tk.Canvas(self.w, width=350, height=150)
        canvas1.pack()
        canvas1.place(relx=0.45, rely=0.10)
        img = ImageTk.PhotoImage(Image.open(path1))
        canvas1.create_image(180, 140, anchor='center', image=img)

        canvas2 = tk.Canvas(self.w, width=600, height=150)
        canvas2.pack()
        canvas2.place(relx=0.10, rely=0.45)
        img2 = ImageTk.PhotoImage(Image.open(path2))
        canvas2.create_image(180, 140, anchor='center', image=img2)

        self.w.mainloop()


window = tk.Tk()
app_data = Data().read_data("Data/Data.json")

img_canvas = ImageObj(window)
app = Interface("DataConfirmationGUI", 800, 600, window, app_data, img_canvas)

app.start()
