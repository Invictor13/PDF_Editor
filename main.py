"""
Arquivo Main - Editor de PDF
Desenvolvido por: Victor Ladislau Viana

0) Biblioetcas Utilizadas:
    -Tkinter = Renderização da Interface Gráfica.
    -pikepdf = Compactação e mesclagem de PDF's.
"""
#Importando as Bibliotecas:
import tkinter as tk
from tkinter import filedialog, messagebox
from software_src.pdf_compactador import compactar_pdf

class PDF_EditorApp:
    # Métodos e Funções (Ações dos botões)
    def click_compactar(self):
        try:
            selecao_pdf = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])

            if selecao_pdf:
                compactar_exportar = selecao_pdf.replace(".pdf","_compactado.pdf")
                selecao_check, mensagem = compactar_pdf(selecao_pdf, compactar_exportar)

                if selecao_check:
                    messagebox.showinfo("Sucesso!", mensagem)
                else:
                    messagebox.showerror("Erro!", mensagem)
        except Exception as e:
            messagebox.showerror("Erro!", f"Ocorreu um erro inesperado: {e}")

    def click_mesclar(self):
        print("Os PDFS serão Mesclados")

    def click_sair(self):
        print("O programa será encerrado")
        self.root.quit()  # Encerra o programa adequadamente
    
    def __init__(self, root):
        self.root = root
        # Configurações da Janela Principal
        self.root.title("Invictor13 - Editor de PDF")
        self.root.state("zoomed")
        
        # Constrói a interface
        self.criar_cabecalho()
        self.criar_frame_apresentacao()
        self.criar_botoes()
        self.criar_rodape()

    def criar_cabecalho(self):
        # Cabeçalho
        self.L_titulo = tk.Label(self.root, text="Invictor13 - Editor de PDF")
        self.L_titulo.pack()
        
        self.L_subtitle = tk.Label(self.root, text="Escolha uma das opções para editar o PDF:")
        self.L_subtitle.pack()

    def criar_frame_apresentacao(self):
        # Frame com bordas para apresentar o projeto
        self.frame_projeto = tk.Frame(self.root, borderwidth=2, relief="groove", padx=10, pady=10)
        self.frame_projeto.pack(pady=20, padx=20)

        descricao = ("Bem-vindo ao Editor de PDF - Invictor13\n\n"
                     "Esta entrega de MVP, possui o objetivo de apresentar:\n"
                     "1) As Bibliotecas utilizadas\n"
                     "2) A criação do layout do Software\n"
                     "3) Disponibilização do repositório no Github.\n"
                     "\n No momento, o software está em desenvolvimento.\n"
                     "Seu progresso pode ser consulado em:https://invictor13.github.io/PDF_Editor/")
        self.L_apresentacao = tk.Label(self.frame_projeto, text=descricao, justify="center", font=("Arial", 12))
        self.L_apresentacao.pack()

    def criar_botoes(self):
        # Frame para alinhar os Botões de Navegação lado a lado
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(pady=20)

        self.B_compactar = tk.Button(self.frame_botoes, text="Compactar PDF", command=self.click_compactar, width="20", height="5")
        self.B_compactar.pack(side=tk.LEFT, padx=15)
        
        self.B_mesclar = tk.Button(self.frame_botoes, text="Mesclar PDF", command=self.click_mesclar, width="20", height="5")
        self.B_mesclar.pack(side=tk.LEFT, padx=15)

        self.B_sair = tk.Button(self.frame_botoes, text="Sair", command=self.click_sair, width="20", height="5")
        self.B_sair.pack(side=tk.LEFT, padx=15)

    def criar_rodape(self):
        # Rodapé
        self.L_titlefooter = tk.Label(self.root, text="Programa desenvolvido por Victor Viana - 2026")
        self.L_titlefooter.pack()
        
        self.L_subtitlefooter = tk.Label(self.root, text="MVP - Editor de PDF V0.1")
        self.L_subtitlefooter.pack()


# Inicialização do App
if __name__ == "__main__":
    janela = tk.Tk()
    app = PDF_EditorApp(janela)
    janela.mainloop()
