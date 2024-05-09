import streamlit as st
from fpdf import FPDF
import base64

def generar_pdf(nombre, email, fecha_inicio, fecha_fin, tipo_permiso, motivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Solicitud de Permiso", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=1)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=1)
    pdf.cell(200, 10, txt=f"Fecha de Inicio: {fecha_inicio}", ln=1)
    pdf.cell(200, 10, txt=f"Fecha de Fin: {fecha_fin}", ln=1)
    pdf.cell(200, 10, txt=f"Tipo de Permiso: {tipo_permiso}", ln=1)
    pdf.cell(200, 10, txt=f"Motivo: {motivo}", ln=1)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return pdf_bytes

def descargar_pdf(pdf_bytes):
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="solicitud_permiso.pdf">Descargar PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("Solicitud de Permiso")
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    fecha_inicio = st.date_input("Fecha de inicio")
    fecha_fin = st.date_input("Fecha de fin")
    tipo_permiso = st.selectbox("Tipo de Permiso", ["Vacaciones", "Baja por Enfermedad", "Día Personal", "Otro"])
    motivo = st.text_area("Motivo del permiso")

    if st.button("Enviar"):
        pdf_bytes = generar_pdf(nombre, email, fecha_inicio, fecha_fin, tipo_permiso, motivo)
        descargar_pdf(pdf_bytes)
        st.success("Envíale este PDF a RRHH")

if __name__ == "__main__":
    main()
