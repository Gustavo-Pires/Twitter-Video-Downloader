import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    quality = quality_var.get()
    save_path = filedialog.askdirectory()

    if not url:
        messagebox.showerror("Erro", "Por favor, forneça um link.")
        return
    
    if not save_path:
        messagebox.showerror("Erro", "Por favor, selecione um diretório para salvar o vídeo.")
        return

    cookies_file = filedialog.askopenfilename(title="Selecione o arquivo de cookies", filetypes=[("Cookies file", "*.txt")])

    if not cookies_file:
        messagebox.showerror("Erro", "Por favor, forneça o arquivo de cookies.")
        return

    ydl_opts = {
        'format': quality,
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'cookiefile': cookies_file,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {str(e)}")

app = tk.Tk()
app.title("Downloader de Vídeos do Twitter")

tk.Label(app, text="URL do Vídeo:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Qualidade:").grid(row=1, column=0, padx=10, pady=10)
quality_var = tk.StringVar(value='best')
quality_menu = tk.OptionMenu(app, quality_var, 'best', 'worst')
quality_menu.grid(row=1, column=1, padx=10, pady=10)

download_button = tk.Button(app, text="Baixar", command=download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
