import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# =========================
# JUDUL & DESKRIPSI
# =========================
st.title("🚀 Simulasi Gerak Parabola Interaktif")

st.write("Simulasi ini menunjukkan gerak parabola, yaitu gabungan gerak horizontal (GLB) dan gerak vertikal (GLBB).")

# =========================
# INPUT
# =========================
v0 = st.slider("Kecepatan awal (m/s)", 1, 100, 20)
sudut = st.slider("Sudut (derajat)", 0, 90, 45)
warna = st.color_picker("Pilih warna lintasan", "#00f900")

# =========================
# PILIH PLANET
# =========================
planet = st.selectbox("Pilih Planet", ["Bumi", "Bulan", "Mars"])

if planet == "Bumi":
    g = 9.8
elif planet == "Bulan":
    g = 1.62
elif planet == "Mars":
    g = 3.7

st.write(f"Gravitasi di {planet} = {g} m/s²")

# =========================
# RUMUS
# =========================
st.subheader("📘 Persamaan Gerak Parabola")
st.latex("x = v_0 \\cos(\\theta) t")
st.latex("y = v_0 \\sin(\\theta) t - \\frac{1}{2} g t^2")

# =========================
# PERHITUNGAN
# =========================
theta = np.radians(sudut)
t = np.linspace(0, 2 * v0 * np.sin(theta) / g, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# =========================
# HASIL
# =========================
waktu_total = 2 * v0 * np.sin(theta) / g
jarak_maks = v0**2 * np.sin(2 * theta) / g
tinggi_maks = (v0**2 * (np.sin(theta))**2) / (2 * g)

st.subheader("📊 Hasil Perhitungan")
st.write(f"Waktu di udara: {waktu_total:.2f} s")
st.write(f"Jarak maksimum: {jarak_maks:.2f} m")
st.write(f"Tinggi maksimum: {tinggi_maks:.2f} m")

# =========================
# ANIMASI
# =========================
st.subheader("🎬 Animasi Gerak Parabola")

col1, col2 = st.columns(2)
start = col1.button("▶️ Play")
reset = col2.button("🔄 Reset")

placeholder = st.empty()
info = st.empty()

if start:
    for i in range(len(x)):
        fig, ax = plt.subplots()
        
        # lintasan
        ax.plot(x, y, '--', color=warna)
        
        # bola
        ax.scatter(x[i], y[i])
        
        ax.set_xlim(0, max(x)+1)
        ax.set_ylim(0, max(y)+1)
        ax.set_xlabel("Jarak (m)")
        ax.set_ylabel("Tinggi (m)")
        ax.set_title("Simulasi Gerak Parabola")
        
        placeholder.pyplot(fig)
        
        # info realtime
        info.write(f"Waktu: {t[i]:.2f} s | x: {x[i]:.2f} m | y: {y[i]:.2f} m")
        
        time.sleep(0.02)

if reset:
    placeholder.empty()
    info.empty()