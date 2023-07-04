#导入库
import requests;
import tkinter as tk;

def new():
    new_blog = tk.Toplevel(root)
    new_blog.geometry('500x300')
    new_blog.title('新建博客')
    new_blog_name=tk.Entry(new_blog,text="请输入博客名")
    new_blog_name.pack()
    br3_text = tk.Label(root,text='',font=("宋体",30))
    br3_text.pack()
    new_blog_theme=tk.Entry(new_blog,text="请输入博客主题")
    new_blog_theme.pack()

root=tk.Tk()
root.geometry("500x300")
root.title("博客制作工具");

logo_text = tk.Label(root,text='博客制作工具',font=("宋体",30))
logo_text.pack()

br2_text = tk.Label(root,text='',font=("宋体",30))
br2_text.pack()

new_bu=tk.Button(root,text="新建博客",command=new)
new_bu.pack()

br1_text = tk.Label(root,text='',font=("宋体",30))
br1_text.pack()

old_bu=tk.Button(root,text="查看博客",command=new)
old_bu.pack()

root.mainloop()