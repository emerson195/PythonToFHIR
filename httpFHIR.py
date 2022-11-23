from asyncio.windows_events import NULL
import urllib.request as request
import json
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
# import requests
# import getData

win = tk.Tk()
win.title("FHIR get observation data")
w, h = win.maxsize()
win.state("zoomed")  # 最大化界面(只有在windows才可以用)
# win.resizable(False, False)  # 不讓使用者調動大小
win.config(bg="white")  # 設定背景顏色

counter = 0  # 判斷要不要清空表格


def submit(counter):
    genename = getData.GetGeneNameData(
        en1.get(), en2.get(), en3.get(), en4.get())

    # Gname = en1.get()
    # aac = en2.get()
    # spe = en3.get()
    # patient = en4.get()

    # if genename.Gname is not "" and genename.aac is "" and genename.spe is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())  # 清空表格

    #     genename.Gname = genename.Gname.upper()  # 強制轉換成大寫

    #     genename.Open_HGNCFile_and_find_HGNCID()
    #     genename.Search_is_related__to_HGNCID()
        # # 讀檔，但路徑會因為放的位置不一樣，所以要再進行調整
        # with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\hgnc_complete_set.json", encoding="utf-8") as new1:
        #     sym = json.load(new1)

    #     i = 0

    #     # 跑所有HGNC代碼表中的代碼
    #     while i < 42422:
    #         if genename.Gname == sym["response"]["docs"][i]["symbol"]:
    #             # $要另外寫，不然HTTP不會給過
    #             Gname1 = "$" + sym["response"]["docs"][i]["hgnc_id"]

    #             src = "http://192.168.50.5:10050/api/Observation?component-code-value-concept=http://loinc.org|48018-6" + Gname1
    #             # "http://192.168.50.5:10050/fhir/Observation?component-code-value-concept=http%%3A%%2F%%2Floinc.org%%7C48018-6%%24HGNC%%3A" + data
    #             # 之前的: src = "https://hapi.fhir.tw"， "http://203.64.84.213:8080/fhir", "http://203.64.84.213:52888/r4/fhir"

    #             # token必須隨post request 附上，Server才會Response要的資料回來
    #             token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #             headers = {
    #                 "authorization": "Bearer " + token  # 帶著存取憑證
    #             }

    #             # 抓取我們需要的json資料
    #             response = requests.get(src, headers=headers)
    #             result = response.json()

    #             # 把json資料寫入檔案中
    #             with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new2.json", "w", encoding="utf-8") as file:
    #                 json.dump(result, file, indent=4)

    #             total = result["total"]  # 判斷資料存不存在

    #             if(total == 0):
    #                 messagebox.showerror("error", "查無資料")

    #             else:
    #                 if(len(result["link"]) != 1):
    #                     linkdata = result["link"][1]["url"]
    #                     linknext = result["link"][1]["relation"]
    #                     while(linknext == "next"):
    #                         j = 0
    #                 # 將查詢到的資料以表格顯示
    #                         while(j < len(result["entry"])):
    #                             treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                            result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                            result["entry"][j]["resource"]["component"][0][
    #                                 "valueCodeableConcept"]["coding"][0]["display"],
    #                                 result["entry"][j]["resource"]["status"],
    #                                 result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                 result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                 result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                 result["entry"][j]["resource"]["effectiveDateTime"]))
    #                             j += 1
    #                         response = requests.get(linkdata, headers=headers)
    #                         result = response.json()

    #                         linkdata = result["link"][1]["url"]
    #                         linknext = result["link"][1]["relation"]

    #                     messagebox.showerror("Finish", "資料查詢完成")

    #                 else:
    #                     j = 0
    #                     while(j < len(result["entry"])):
    #                         treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                        result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                        result["entry"][j]["resource"]["component"][0][
    #                                                            "valueCodeableConcept"]["coding"][0]["display"],
    #                                                        result["entry"][j]["resource"]["status"],
    #                                                        result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["component"][1][
    #                                                            "valueCodeableConcept"]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["effectiveDateTime"]))
    #                         j += 1
    #                     messagebox.showerror("Finish", "資料查詢完成")
    #             break
    #         i += 1

    #     if(i >= 42422):
    #         messagebox.showerror("errorbox", "查無資料")

    # elif aac is not "" and Gname is "" and spe is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())

    #     aac1 = "$" + aac
    #     src = "http://192.168.50.5:10050/api/Observation?component-code-value-concept=http://loinc.org|48005-3" + aac1

    #     token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #     headers = {
    #         "authorization": "Bearer " + token  # 帶著存取憑證
    #     }

    #     # 抓取我們需要的json資料
    #     response = requests.get(src, headers=headers)
    #     result = response.json()

    #     total = result["total"]

    #     if total != 0:
    #         with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new3.json", "w") as file:
    #             json.dump(result, file, indent=4)

    #         if(len(result["link"]) != 1):
    #             linkdata = result["link"][1]["url"]
    #             linknext = result["link"][1]["relation"]
    #             while(linknext == "next"):
    #                 j = 0
    #                 # 將查詢到的資料以表格顯示
    #                 while(j < len(result["entry"])):
    #                     treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                    result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                    result["entry"][j]["resource"]["component"][0][
    #                         "valueCodeableConcept"]["coding"][0]["display"],
    #                         result["entry"][j]["resource"]["status"],
    #                         result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["effectiveDateTime"]))
    #                     j += 1
    #                 response = requests.get(linkdata, headers=headers)
    #                 result = response.json()

    #                 linkdata = result["link"][1]["url"]
    #                 linknext = result["link"][1]["relation"]

    #             messagebox.showerror("Finish", "資料查詢完成")

    #         else:
    #             j = 0
    #             while(j < len(result["entry"])):
    #                 treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                result["entry"][j]["resource"]["component"][0]["valueCodeableConcept"]["coding"][0]["display"],
    #                                                result["entry"][j]["resource"]["status"],
    #                                                result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["effectiveDateTime"]))
    #                 j += 1
    #             messagebox.showerror("Finish", "資料查詢完成")

    #     else:
    #         messagebox.showerror("errorbox", "查無資料")

    # elif spe is not "" and Gname is "" and aac is "" and patient is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())  # 清空表格

    #     src = "http://192.168.50.5:10050/api/Observation?specimen=" + spe

    #     token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #     headers = {
    #         "authorization": "Bearer " + token  # 帶著存取憑證
    #     }

    #     # 抓取我們需要的json資料
    #     response = requests.get(src, headers=headers)
    #     result = response.json()

    #     # 把json資料寫入檔案中
    #     with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new4.json", "w", encoding="utf-8") as file:
    #         json.dump(result, file, indent=4)

    #     total = result["total"]  # 計算共有幾筆資料
    #     # print(total)

    #     if(total == 0):
    #         messagebox.showerror("error", "查無資料")

    #     else:
    #         if(len(result["link"]) != 1):
    #             linkdata = result["link"][1]["url"]
    #             linknext = result["link"][1]["relation"]
    #             while(linknext == "next"):
    #                 j = 0
    #                 # 將查詢到的資料以表格顯示
    #                 while(j < len(result["entry"])):
    #                     treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                    result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                    result["entry"][j]["resource"]["component"][0][
    #                         "valueCodeableConcept"]["coding"][0]["display"],
    #                         result["entry"][j]["resource"]["status"],
    #                         result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                         result["entry"][j]["resource"]["effectiveDateTime"]))
    #                     j += 1
    #                 response = requests.get(linkdata, headers=headers)
    #                 result = response.json()

    #                 linkdata = result["link"][1]["url"]
    #                 linknext = result["link"][1]["relation"]

    #             messagebox.showerror("Finish", "資料查詢完成")

    #         else:
    #             j = 0
    #             while(j < len(result["entry"])):
    #                 treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                result["entry"][j]["resource"]["component"][0]["valueCodeableConcept"]["coding"][0]["display"],
    #                                                result["entry"][j]["resource"]["status"],
    #                                                result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["effectiveDateTime"]))
    #                 j += 1
    #             messagebox.showerror("Finish", "資料查詢完成")

    # # 查patient ID
    # elif patient is not "" and Gname is "" and aac is "" and spe is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())  # 清空表格
    #     src = "http://192.168.50.5:10050/api/Observation?patient=" + patient

    #     token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #     headers = {
    #         "authorization": "Bearer " + token  # 帶著存取憑證
    #     }

    #     # 抓取我們需要的json資料
    #     response = requests.get(src, headers=headers)
    #     result = response.json()

    #     # 把json資料寫入檔案中
    #     with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new13.json", "w", encoding="utf-8") as file:
    #         json.dump(result, file, indent=4)

    #     total = result["total"]  # 計算共有幾筆資料

    #     if(total == 0):
    #         messagebox.showerror("error", "查無資料")

    #     else:
    #         if(len(result["link"]) != 1):
    #             linkdata = result["link"][1]["url"]
    #             linknext = result["link"][1]["relation"]
    #             while(linknext == "next"):
    #                 j = 0

    #                 # 將查詢到的資料以表格顯示
    #                 while(j < len(result["entry"])):
    #                     treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                    result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                    result["entry"][j]["resource"]["component"][0][
    #                                                        "valueCodeableConcept"]["coding"][0]["display"],
    #                                                    result["entry"][j]["resource"]["status"],
    #                                                    result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["effectiveDateTime"]))
    #                     j += 1
    #                 response = requests.get(linkdata, headers=headers)
    #                 result = response.json()

    #                 linkdata = result["link"][1]["url"]
    #                 linknext = result["link"][1]["relation"]

    #             messagebox.showerror("Finish", "資料查詢完成")

    #         else:
    #             j = 0
    #             while(j < len(result["entry"])):
    #                 treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                result["entry"][j]["resource"]["component"][0]["valueCodeableConcept"]["coding"][0]["display"],
    #                                                result["entry"][j]["resource"]["status"],
    #                                                result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["effectiveDateTime"]))
    #                 j += 1
    #             messagebox.showerror("Finish", "資料查詢完成")

    # elif spe is not "" and patient is not "" and Gname is "" and aac is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())  # 清空表格
    #     src = "http://192.168.50.5:10050/api/Observation?patient=" + \
    #         patient + "&" + "specimen=" + spe

    #     token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #     headers = {
    #         "authorization": "Bearer " + token  # 帶著存取憑證
    #     }

    #     # 抓取我們需要的json資料
    #     response = requests.get(src, headers=headers)
    #     result = response.json()

    #     # 把json資料寫入檔案中
    #     with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new14.json", "w", encoding="utf-8") as file:
    #         json.dump(result, file, indent=4)

    #     total = result["total"]  # 計算共有幾筆資料
    #     # print(total)

    #     if(total == 0):
    #         messagebox.showerror("error", "查無資料")

    #     else:
    #         if(len(result["link"]) != 1):
    #             linkdata = result["link"][1]["url"]
    #             linknext = result["link"][1]["relation"]
    #             while(linknext == "next"):
    #                 j = 0
    #         # 將查詢到的資料以表格顯示
    #                 while(j < len(result["entry"])):
    #                     treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                    result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                    result["entry"][j]["resource"]["component"][0][
    #                                                        "valueCodeableConcept"]["coding"][0]["display"],
    #                                                    result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["status"],
    #                                                    result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                    result["entry"][j]["resource"]["effectiveDateTime"]))
    #                     j += 1
    #                 response = requests.get(linkdata, headers=headers)
    #                 result = response.json()

    #                 linkdata = result["link"][1]["url"]
    #                 linknext = result["link"][1]["relation"]

    #             messagebox.showerror("Finish", "資料查詢完成")

    #         else:
    #             j = 0
    #             while(j < len(result["entry"])):
    #                 treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                result["entry"][j]["resource"]["component"][0]["valueCodeableConcept"]["coding"][0]["display"],
    #                                                result["entry"][j]["resource"]["status"],
    #                                                result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["component"][1]["valueCodeableConcept"]["coding"][0]["code"],
    #                                                result["entry"][j]["resource"]["effectiveDateTime"]))
    #                 j += 1
    #             messagebox.showerror("Finish", "資料查詢完成")

    # # 抓 patient id specimen id and Gene name
    # elif patient is not "" and spe is not "" and Gname is not "" and aac is "":
    #     if(counter == 2):
    #         treeview.delete(*treeview.get_children())  # 清空表格
    #     # 讀檔，但路徑會因為放的位置不一樣，所以要再進行調整
    #     with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\hgnc_complete_set.json", encoding="utf-8") as new1:
    #         sym = json.load(new1)

    #     i = 0

    #     # 跑所有HGNC代碼表中的代碼
    #     while i < 42422:
    #         if Gname == sym["response"]["docs"][i]["symbol"]:
    #             # $要另外寫，不然HTTP不會給過
    #             Gname1 = "$" + sym["response"]["docs"][i]["hgnc_id"]

    #             src = "http://192.168.50.5:10050/api/Observation?patient=" + \
    #                 patient + "&" + "specimen=" + spe + "&" + \
    #                 "component-code-value-concept=http://loinc.org|48018-6" + Gname1

    #             token = "2eedd6db-26d5-4f93-9b06-50ff6a2c0ad0"
    #             headers = {
    #                 "authorization": "Bearer " + token  # 帶著存取憑證
    #             }

    #             # 抓取我們需要的json資料
    #             response = requests.get(src, headers=headers)
    #             result = response.json()

    #             # 把json資料寫入檔案中
    #             with open("D:\\程式資料\\FHIR Genomic 基因定序資料\\python 版本\\new15.json", "w", encoding="utf-8") as file:
    #                 json.dump(result, file, indent=4)

    #             total = result["total"]  # 判斷資料存不存在

    #             if(total == 0):
    #                 messagebox.showerror("error", "查無資料")

    #             else:
    #                 if(len(result["link"]) != 1):
    #                     linkdata = result["link"][1]["url"]
    #                     linknext = result["link"][1]["relation"]
    #                     while(linknext == "next"):
    #                         j = 0
    #                 # 將查詢到的資料以表格顯示
    #                         while(j < len(result["entry"])):
    #                             treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                            result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                            result["entry"][j]["resource"]["component"][0][
    #                                                                "valueCodeableConcept"]["coding"][0]["display"],
    #                                                            result["entry"][j]["resource"]["status"],
    #                                                            result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                            result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                            result["entry"][j]["resource"]["component"][1][
    #                                                                "valueCodeableConcept"]["coding"][0]["code"],
    #                                                            result["entry"][j]["resource"]["effectiveDateTime"]))
    #                             j += 1
    #                         response = requests.get(linkdata, headers=headers)
    #                         result = response.json()

    #                         linkdata = result["link"][1]["url"]
    #                         linknext = result["link"][1]["relation"]

    #                     messagebox.showerror("Finish", "資料查詢完成")

    #                 else:
    #                     j = 0
    #                     while(j < len(result["entry"])):
    #                         treeview.insert("", j, values=(result["entry"][j]["resource"]["id"],
    #                                                        result["entry"][j]["resource"]["specimen"]["reference"],
    #                                                        result["entry"][j]["resource"]["component"][0][
    #                                                            "valueCodeableConcept"]["coding"][0]["display"],
    #                                                        result["entry"][j]["resource"]["status"],
    #                                                        result["entry"][j]["resource"]["category"][0]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["code"]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["component"][1][
    #                                                            "valueCodeableConcept"]["coding"][0]["code"],
    #                                                        result["entry"][j]["resource"]["effectiveDateTime"]))
    #                         j += 1
    #                     messagebox.showerror("Finish", "資料查詢完成")
    #             break
    #         i += 1

    #     if(i >= 42422):
    #         messagebox.showerror("errorbox", "查無資料")

    # else:
    #     messagebox.showerror("errorbox", "輸入錯誤")


lb1 = tk.Label(win, text="GeneName", bg="white")
lb1.place(anchor="nw", x=0, y=0)

en1 = tk.Entry(win, bg="white")
en1.place(anchor="nw", x=100, y=0)

lb2 = tk.Label(win, text="Amino Acid Change", bg="white")
lb2.place(anchor="nw", x=250, y=0)

en2 = tk.Entry(win, bg="white")
en2.place(anchor="nw", x=380, y=0)

lb3 = tk.Label(win, text="specimen", bg="white")
lb3.place(anchor="nw", x=530, y=0)

en3 = tk.Entry(win, bg="white")
en3.place(anchor="nw", x=600, y=0)

lb4 = tk.Label(win, text="patient ID", bg="white")
lb4.place(anchor="nw", x=0, y=50)

en4 = tk.Entry(win, bg="white")
en4.place(anchor="nw", x=100, y=50)

lb5 = tk.Label(win, text="GenomicSourceClass", bg="white")
lb5.place(anchor="nw", x=250, y=50)

en4 = tk.Entry(win, bg="white")
en4.place(anchor="nw", x=380, y=50)

lb5 = tk.Label(win, text="GenomicDNAChange", bg="white")
lb5.place(anchor="nw", x=530, y=50)

en5 = tk.Entry(win, bg="white")
en5.place(anchor="nw", x=660, y=50)


counter += 2
btn = tk.Button(text="送出", command=lambda: submit(counter))
btn.place(anchor="nw", x=800, y=0)


columns = ("Observation ID", "樣本ID", "基因名稱",
           "status", "category", "code",  "氨基酸變異", "effectiveDateTime")
treeview = ttk.Treeview(win, show="headings", height=28, columns=columns)  # 表格

treeview.column("Observation ID", width=100, anchor='center')  # 表示列,不显示
treeview.column("樣本ID", width=200, anchor='center')
treeview.column("基因名稱", width=100, anchor='center')
treeview.column("status", width=100, anchor='center')
treeview.column("category", width=100, anchor='center')
treeview.column("code", width=100, anchor='center')
treeview.column("氨基酸變異", width=200, anchor='center')
treeview.column("effectiveDateTime", width=200, anchor='center')

treeview.heading("Observation ID", text="Observation ID")  # 显示表头
treeview.heading("樣本ID", text="樣本ID")
treeview.heading("基因名稱", text="基因名稱")
treeview.heading("status", text="status")
treeview.heading("category", text="category")
treeview.heading("code", text="code")
treeview.heading("氨基酸變異", text="氨基酸變異")
treeview.heading("effectiveDateTime", text="effectiveDateTime")

treeview.place(anchor="n", x=650, y=100)

win.mainloop()
