
import streamlit as st
from datetime import datetime
from supabase import create_client, Client

# Configuración de Supabase (reemplazar con tus claves reales)
SUPABASE_URL = "https://owfpruyynhwfwmoswtyx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im93ZnBydXl5bmh3Zndtb3N3dHl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzNTAwNjQsImV4cCI6MjA2MzkyNjA2NH0.rH-vDwm02GTIftq-yT53a-mVcr43lPiOcD_F_NDErUU"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Formulario Docente - Registro", layout="centered")

st.markdown("<h2 style='color:#3366cc;'>📝 Registro de Observaciones Docentes</h2>", unsafe_allow_html=True)
st.write("Complete este formulario por cada alumno y espacio curricular correspondiente. Los datos se guardan directamente en la base institucional.")

# Formulario principal
with st.form("formulario_alumno"):
    espacio = st.text_input("📚 Espacio Curricular")
    nombre_alumno = st.text_input("👤 Nombre y Apellido del Alumno")
    curso_division = st.text_input("🏫 Curso y División (Ej: 3°A)")
    edad = st.number_input("🎂 Edad", min_value=10, max_value=25)

    material = st.radio("📘 ¿Cuenta con el material didáctico necesario?", ["Sí", "No"])
    trabaja = st.selectbox("💼 Nivel de trabajo en clase", ["Alto", "Medio", "Bajo"])
    tareas = st.radio("📝 ¿Resuelve las tareas?", ["Sí", "No"])
    tardanza = st.radio("⏰ ¿Tiene tardanzas frecuentes?", ["Sí", "No"])
    respeto = st.radio("🙋 ¿Muestra respeto ante el docente?", ["Sí", "No"])
    carpeta = st.selectbox("📒 Estado de la carpeta o apuntes", ["Muy bien", "Regular", "Incompleta"])
    faltas_conducta = st.number_input("⚠️ Cantidad de faltas de conducta", min_value=0)
    equipo = st.selectbox("🤝 Trabajo en equipo", ["Bueno", "Regular", "Malo"])
    interes = st.radio("👀 ¿Se muestra interesado a trabajar en clase?", ["Sí", "No"])
    manejo = st.selectbox("🔧 Manejo de herramientas y máquinas (solo taller)", ["Bueno", "Regular", "Malo"])
    epp = st.radio("🦺 ¿Usa elementos de protección personal? (solo taller)", ["Sí", "No"])
    material_taller = st.radio("📦 ¿Trae el material para trabajar en taller?", ["Sí", "No"])
    convivencia = st.radio("📏 ¿Cumple con las normas de convivencia?", ["Sí", "No"])

    enviado = st.form_submit_button("✅ Enviar Registro")

if enviado:
    nuevo_registro = {
        "fecha_hora": datetime.now().isoformat(),
        "espacio_curricular": espacio,
        "nombre_alumno": nombre_alumno,
        "curso_division": curso_division,
        "edad": edad,
        "material_didactico": material,
        "trabajo_en_clase": trabaja,
        "resolucion_tareas": tareas,
        "tardanza_frecuente": tardanza,
        "respeto_docente": respeto,
        "carpeta": carpeta,
        "faltas_conducta": faltas_conducta,
        "trabajo_equipo": equipo,
        "interes": interes,
        "manejo_taller": manejo,
        "usa_epp": epp,
        "material_taller": material_taller,
        "normas_convivencia": convivencia
    }

    try:
        data, count = supabase.table("formulario_docente").insert(nuevo_registro).execute()
        st.success("✅ Registro guardado correctamente en Supabase.")
    except Exception as e:
        st.error(f"❌ Error al guardar en Supabase: {e}")
