"""
Para criarmos essa função de compactar PDF, utilziaremos a biblioteca Pikpdf.
Por se tratar de uma biblioteca com uma licença que permite o uso comercial, é uma ótima opção para o nosso software.
"""
import pikepdf

def compactar_pdf(selecao_pdf, compactar_exportar):
    try:
        with pikepdf.open(selecao_pdf) as arquivo:
            arquivo.save(compactar_exportar, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
            return True, f"PDF Compactado com sucesso!: {compactar_exportar}"
    except Exception as e:
        return False, f"Erro ao compactar PDF: {e}"
  