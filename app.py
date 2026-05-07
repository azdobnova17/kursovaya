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

.blue {
    background: rgba(219,234,254,0.65);
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #93c5fd;
    margin-bottom: 10px;
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
    background: #e9fff3;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #9be7c4;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📊 Вычисление интеграла</div>', unsafe_allow_html=True)

st.divider()

with st.container():
    st.markdown('<div class="blue">', unsafe_allow_html=True)

    st.markdown("### 📌 Что такое интеграл")

    st.markdown("""
    Интеграл — это способ найти площадь под графиком функции на отрезке.  
    Он показывает суммарное накопление значений функции.
    """)

    st.markdown("""
    📌 Функции:
    - x²  
    - sin(x)  
    - cos(x)  
    - eˣ  
    """)

    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="blue">', unsafe_allow_html=True)

    st.markdown("### 📌 Численное вычисление интеграла")

    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum_{i=1}^{n} f(x_i)\cdot h")
    st.latex(r"h = \frac{b-a}{n}")

    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="blue">', unsafe_allow_html=True)

    st.markdown("### 📌 1. Левые прямоугольники")

    st.markdown("""
Метод использует значение функции в левой точке каждого отрезка.

📌 Особенности:
- часто даёт занижение площади
- быстрее считается
- ошибка уменьшается при увеличении n
""")

    st.latex(r"x_i = a + (i-1)\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_i)\cdot h")

    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="blue">', unsafe_allow_html=True)

    st.markdown("### 📌 2. Правые прямоугольники")

    st.markdown("""
Метод использует значение функции в правой точке каждого отрезка.

📌 Особенности:
- часто даёт завышение площади
- чувствителен к росту функции
- простая реализация
""")

    st.latex(r"x_i = a + i\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_i)\cdot h")

    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="blue">', unsafe_allow_html=True)

    st.markdown("### 📌 3. Средние прямоугольники")

    st.markdown("""
Метод использует значение функции в середине отрезка.

📌 Особенности:
- самый точный метод
- балансирует ошибку левого и правого
- используется в инженерных задачах
""")

    st.latex(r"x_i = a + (i - 0.5)\cdot h")
    st.latex(r"\int_{a}^{b} f(x)\,dx \approx \sum f(x_{i+1/2})\cdot h")

    st.markdown('</div>', unsafe_allow_html=True)


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

    with st.container():
        st.markdown('<div class="blue">', unsafe_allow_html=True)

        st.markdown("### 📌 Решение с подстановкой значений")

        st.latex(fr"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

        st.markdown("### 📌 Первые шаги:")

        preview_n = min(5, n)

        for i in range(preview_n):

            x = get_x(a, h, i, method)
            fx = f(x, function_name)
            area = fx * h

            st.markdown(
                f"""
**i = {i+1}**

xᵢ = {x:.4f}  
f(xᵢ) = {fx:.4f}  
Sᵢ = {area:.4f}
"""
            )

        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown(f'<div class="result">Интеграл ≈ {sum_result}</div>', unsafe_allow_html=True)

    st.balloons()