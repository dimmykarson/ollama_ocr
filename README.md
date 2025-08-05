````markdown
# OCR LLama 🦙 — Granite 3-Vision PDF OCR

OCR LLama é um micro-projeto Python que demonstra como extrair texto de
PDFs usando **Granite 3.2-Vision** (via
[ollama-ocr](https://pypi.org/project/ollama-ocr/)) hospedado em uma
instância **Ollama** local ou remota.

> **Principais pontos**
>
> * Conexão automática ao servidor Ollama definido na variável
>   `OLLAMA_HOST`; se não existir, cai em `http://localhost:11434`.
> * Prompt padrão em **PT-BR**, mas pode mudar para *markdown*, *json*,
>   *table* etc.
> * Exemplo de uso em `app/main.py` e testes automatizados em `tests/`.

---

## Índice

1. [Pré-requisitos](#pré-requisitos)  
2. [Instalação](#instalação)  
3. [Variáveis de ambiente](#variáveis-de-ambiente)  
4. [Como usar](#como-usar)  
5. [Estrutura do projeto](#estrutura-do-projeto)  
6. [Testes](#testes)  
7. [Licença](#licença)

---

## Pré-requisitos

| Item | Versão mínima | Observação |
|------|---------------|-----------|
| Python | 3.9 | Compatível 3.9 – 3.12 |
| Ollama | 0.1.38 | Rodando o modelo **granite3.2-vision** |
| poppler-utils | 22.0 | Necessário para converter páginas do PDF em imagens |

Instale o Poppler em Alma Linux/CentOS Stream:

```bash
sudo dnf install -y poppler-utils
````

---

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/orc_llama.git
cd orc_llama
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

> O `requirements.txt` inclui `ollama-ocr>=0.1.4` e `python-dotenv`.

---

## Variáveis de ambiente

Crie um arquivo **`.env`** na raiz (opcional):

```dotenv
# .env
```

* **Ausente ou vazio** → o app usa `http://localhost:11434`.
* O script compõe automaticamente a URL completa:
  `http(s)://<host>:<porta>/api/generate`.

---

## Como usar

1. **Suba o Ollama** com o modelo Granite 3-Vision:

   ```bash
   ollama pull granite3.2-vision
   OLLAMA_HOST=0.0.0.0:11434 ollama serve
   ```

2. **Execute o exemplo**:

   ```bash
   python app/main.py
   ```

3. Saída esperada:

   ```text
   No. of pages in the PDF: 9
   [..texto extraído em PT-BR..]
   ```

### Adaptando o script

```python
ocr = OCRProcessor(
    model_name="llama3.2-vision",
    base_url=f"{host}/api/generate",
    language="por",               # ou "eng", "spa", "auto"
    # custom_prompt="Escreva tudo em minúsculas"
)

texto = ocr.process_image(
    image_path="data/example.pdf",
    format_type="markdown"        # text | json | table | …
)
```

---

## Estrutura do projeto

```
.
├── app
│   ├── __init__.py      # marca pasta como módulo
│   ├── main.py          # ponto de entrada | exemplo de uso
│   └── ocr_pdf.py       # classe OCRParser que encapsula OCRProcessor
├── data
│   └── example.pdf
├── tests                # pytest – cobre casos de sucesso e falha
├── requirements.txt
├── LICENSE
└── README.md            # este arquivo
```

---

## Testes

```bash
pytest -q
```

Os testes verificam:

* Carregamento do `.env` e fallback para `localhost`.
* Conversão de PDF pequeno.
* Manuseio de exceções (ex.: servidor fora do ar).

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

**Dúvidas ou contribuições?**
Abra uma *issue* ou *pull request* — ficarei feliz em colaborar! ✨

```

::contentReference[oaicite:0]{index=0}
```
