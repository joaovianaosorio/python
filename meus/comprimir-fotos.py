import os
from PIL import Image

# Qualidade da compressão (de 1 a 100). 80 é excelente e reduz muito o tamanho.
QUALIDADE = 80

# Largura máxima (mantendo a proporção). Deixe None para manter o tamanho original em pixels.
LARGURA_MAXIMA = 1600 

def comprimir_imagens():
    pasta_atual = os.getcwd()
    pasta_saida = os.path.join(pasta_atual, "compactadas")
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        
    extensoes_validas = (".jpg", ".jpeg", ".png")
    
    total = 0
    for arquivo in os.listdir(pasta_atual):
        if arquivo.lower().endswith(extensoes_validas):
            caminho_entrada = os.path.join(pasta_atual, arquivo)
            caminho_saida = os.path.join(pasta_saida, arquivo)
            
            try:
                with Image.open(caminho_entrada) as img:
                    # Converte para RGB se estiver em RGBA (evita erro ao salvar JPG)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                        
                    # Redimensiona se necessário mantendo a proporção
                    if LARGURA_MAXIMA and img.width > LARGURA_MAXIMA:
                        proporcao = LARGURA_MAXIMA / img.width
                        nova_altura = int(img.height * proporcao)
                        img = img.resize((LARGURA_MAXIMA, nova_altura), Image.Resampling.LANCZOS)
                        
                    # Salva com compressão otimizada
                    img.save(caminho_saida, "JPEG", quality=QUALIDADE, optimize=True)
                    print(f"[OK] Comprimido: {arquivo}")
                    total += 1
            except Exception as e:
                print(f"[Erro] Falha ao processar {arquivo}: {e}")
                
    print(f"\nProcesso concluído! {total} imagens compactadas foram salvas na pasta 'compactadas'.")

if __name__ == "__main__":
    comprimir_imagens()
