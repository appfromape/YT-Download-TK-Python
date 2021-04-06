import tkinter as tk
from pytube import YouTube

# download function
def rbVideo():
    global get_video
    
    get_video = videorb.get()
    label_msg.config(text = f'你選擇的是：{get_video}')
    
def clickDown():
    global get_video
    
    label_msg.config(text = "")
    
    if(url.get() == ""):
        label_msg.config(text = "網址必須填寫!!!")
        return
    
    if (path.get() == ""):
        pathdir = 'download'
    else:
        pathdir = path.get()
        pathdir = pathdir.replace("\\", "\\\\") 
        
    try:
        yt = YouTube(url.get())
        yt.streams.filter(res = get_video, progressive = True).first().download(pathdir)
        label_msg.config(text = "下載完成!!!")
    except:
        label_msg.config(text = "影片下載失敗!!!")


# interface
win = tk.Tk()
win.geometry("700x280")
win.title("YouTube 下載器")  
get_video = "1080p"
videorb = tk.StringVar()
url = tk.StringVar()
path = tk.StringVar()

label_1 = tk.Label(win, text = "Youtube 網址：")
label_1.place(x = 123, y = 30)
entryUrl = tk.Entry(win, textvariable = url)
entryUrl.config(width = 45)
entryUrl.place(x = 220, y= 30)

label_2 = tk.Label(win, text = "下載路徑(預設為 Download):")
label_2.place(x = 40, y = 70)
entry_Path = tk.Entry(win, textvariable = path)
entry_Path.config(width = 45)
entry_Path.place(x = 220, y = 70)

btndown = tk.Button(win, text = "下載影片", command = clickDown)
btndown.place(x = 300, y = 120)

rb_1 = tk.Radiobutton(win, text = "720p, mp4", variable = videorb, value = "720p", command = rbVideo)
rb_1.place(x = 300, y = 170)
rb_1.select()

rb_2 = tk.Radiobutton(win, text = "1080p, mp4", variable = videorb, value = "1080p", command = rbVideo)
rb_2.place(x = 300, y = 190)
rb_2.select()

label_msg = tk.Label(win, text = "", fg = "red")
label_msg.place(x = 300, y = 220)

print(get_video)

win.mainloop()