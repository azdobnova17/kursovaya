import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Интеграл методом прямоугольников",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #eaf2ff, #fff1f7, #f5f9ff, #ffffff);
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: #4f6ef7;
    text-shadow: 0 3px 15px rgba(79,110,247,0.25);
}

.card {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    border: 1px solid rgba(147, 197, 253, 0.35);
}

.blue {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

.pink {
    background: linear-gradient(135deg, #ede9fe, #f5f3ff);
}

.stButton > button {
    background: linear-gradient(135deg, #7c8cff, #ff9ecb);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: 700;
    border: none;
}

.result {
    background: linear-gradient(135deg, #dcfce7, #ecfdf5);
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #9be7c4;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📊 Вычисление интеграла</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; font-size:18px; color:#64748b; margin-bottom:10px;">
Методом прямоугольников
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# ТЕОРИЯ ВО ВКЛАДКЕ
# =========================

with st.expander("📚 Теоретическая часть"):

    with st.container():
        st.markdown("""
        <div class="card blue">

        ### 📌 Что такое интеграл

        Интеграл — это способ найти площадь под графиком функции на отрезке.  
        Он показывает суммарное накопление значений функции.

        Метод прямоугольников — численный метод, где площадь разбивается на маленькие прямоугольники и суммируется.

        📌 Функции:
        - x²
        - sin(x)
        - cos(x)
        - eˣ

        </div>
        """, unsafe_allow_html=True)

    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum_{i=1}^{n} f(x_i)\cdot h")
    st.latex(r"h = \frac{b-a}{n}")

    with st.container():
        st.markdown("""
        <div class="card pink">

        ### 📌 1. Левые прямоугольники

        Метод использует значение функции в левой точке каждого отрезка.

        📌 Особенности:
        - часто даёт занижение площади
        - быстрее считается
        - ошибка уменьшается при увеличении n

        </div>
        """, unsafe_allow_html=True)

    st.latex(r"x_i = a + (i-1)\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_i)\cdot h")

    with st.container():
        st.markdown("""
        <div class="card blue">

        ### 📌 2. Правые прямоугольники

        Метод использует значение функции в правой точке каждого отрезка.

        📌 Особенности:
        - часто даёт завышение площади
        - чувствителен к росту функции
        - простая реализация

        </div>
        """, unsafe_allow_html=True)

    st.latex(r"x_i = a + i\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_i)\cdot h")

    with st.container():
        st.markdown("""
        <div class="card pink">

        ### 📌 3. Средние прямоугольники

        Метод использует значение функции в середине отрезка.

        📌 Особенности:
        - самый точный метод
        - балансирует ошибку
        - используется в инженерных задачах

        </div>
        """, unsafe_allow_html=True)

    st.latex(r"x_i = a + (i - 0.5)\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_{i+1/2})\cdot h")


def f(x, function_name):
    if function_name == "x^2":
        return x ** 2
    elif function_name == "sin(x)":
        return np.sin(x)
    elif function_name == "cos(x)":
        return np.cos(x)
    elif function_name == "e^x":
        return np.exp(x)


def get_x(a, h, i, method):
    if method == "Левые прямоугольники":
        return a + i * h
    elif method == "Правые прямоугольники":
        return a + (i + 1) * h
    elif method == "Средние прямоугольники":
        return a + (i + 0.5) * h


function_name = st.selectbox(
    "Выберите функцию",
    ["x^2", "sin(x)", "cos(x)", "e^x"]
)

method = st.selectbox(
    "Выберите метод",
    ["Левые прямоугольники", "Правые прямоугольники", "Средние прямоугольники"]
)

col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("Начало (a)", value=0.0)
with col2:
    b = st.number_input("Конец (b)", value=1.0)
with col3:
    n = st.number_input("Разбиения (n)", value=10)

if st.button("🚀 Вычислить", use_container_width=True):

    n = int(n)
    h = (b - a) / n

    sum_result = 0

    fig, ax = plt.subplots()

    x_vals = np.linspace(a, b, 400)
    ax.plot(x_vals, f(x_vals, function_name), color="#4f6ef7")

    placeholder = st.empty()

    for i in range(n):

        x = get_x(a, h, i, method)
        fx = f(x, function_name)
        sum_result += fx * h

        ax.bar(
            x,
            fx,
            width=h,
            align='edge',
            color="#60a5fa",
            alpha=0.5
        )

        placeholder.pyplot(fig)
        time.sleep(0.1)

    # =========================
    # ПОШАГОВОЕ РЕШЕНИЕ ВО ВКЛАДКЕ
    # =========================

    with st.expander("📝 Пошаговое решение"):

        with st.container():
            st.markdown("""
            <div class="card blue">

            ### 📌 Решение с подстановкой значений

            </div>
            """, unsafe_allow_html=True)

            st.latex(fr"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

            with st.container():
                st.markdown("""
                <div class="card pink">

                ### 📌 Первые шаги

                </div>
                """, unsafe_allow_html=True)

            preview_n = min(5, n)

            for i in range(preview_n):
                x = get_x(a, h, i, method)
                fx = f(x, function_name)
                area = fx * h

                st.markdown(f"""
i = {i+1}

xᵢ = {x:.4f}  
f(xᵢ) = {fx:.4f}  
Sᵢ = {area:.4f}
""")

    st.markdown(f'<div class="result">Интеграл ≈ {sum_result}</div>', unsafe_allow_html=True)

    st.balloons()