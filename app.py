"""
Dunas Fleet · WMS 3D
Aplicação Streamlit que serve o visualizador 3D do CD.

COMO RODAR:
  pip install streamlit
  streamlit run app.py

Para publicar no Streamlit Cloud:
  1. Suba app.py + wms3d.html para um repositório GitHub público
  2. Acesse share.streamlit.io → New app → aponte para o repo
  3. Clique em Deploy
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Configuração da página ──────────────────────────────
st.set_page_config(
    page_title="Dunas Fleet · WMS 3D",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Remove padding padrão do Streamlit para o 3D ocupar tela toda ──
st.markdown("""
<style>
  /* Remove margens do Streamlit para o canvas 3D usar tela cheia */
  [data-testid="stAppViewContainer"] { padding: 0 !important; }
  [data-testid="stHeader"]           { display: none !important; }
  [data-testid="stToolbar"]          { display: none !important; }
  .block-container                   { padding: 0 !important; max-width: 100% !important; }
  footer                             { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Carrega o HTML do WMS 3D ────────────────────────────
html_file = Path(__file__).parent / "wms3d.html"

if not html_file.exists():
    st.error("❌ Arquivo wms3d.html não encontrado na mesma pasta do app.py")
    st.stop()

html_content = html_file.read_text(encoding="utf-8")

# ── Renderiza o visualizador 3D em tela cheia ───────────
components.html(
    html_content,
    height=900,    # altura em pixels — ajuste conforme sua tela
    scrolling=False,
)