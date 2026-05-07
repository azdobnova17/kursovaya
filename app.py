import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Интеграл методом прямоугольников",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #5b7cfa;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #7a8aa8;
}

.block {
    background-color: #f4f7ff;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #d9e2ff;
    color: #2c3e50;
}

.result-box {
    background-color: #e9f8ef;
    padding: 12px;
    border-radius: 10px;
    color: #1e7a4a;
    font-weight: bold;
    border: 1px solid #bfe8cf;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 Вычисление интеграла</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Метод прямоугольников</div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="block">
📌 <b>Выбор функции</b> определяет график, под которым считается интеграл.<br><br>
x² → парабола<br>
sin(x) → синус<br>
cos(x) → косинус<br>
eˣ → экспонента
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="block">
📌 <b>Метод прямоугольников</b><br><br>

Разбиение интервала [a, b] на n частей и суммирование площадей прямоугольников.

<br><br>

<b>Формулы:</b><br>

$$
h = \\frac{b - a}{n}
$$

$$
I \\approx \\sum_{i=0}^{n-1} f(a + i \\cdot h) \\cdot h
$$

</div>
""", unsafe_allow_html=True)

def f(x, function_name):
    if function_name == "x^2":
        return x ** 2
    elif function_name == "sin(x)":
        return np.sin(x)
    elif function_name == "cos(x)":
        return np.cos(x)
    elif function_name == "e^x":
        return np.exp(x)

def plot_graph(a, b, n, function_name):
    x = np.linspace(a, b, 400)
    y = f(x, function_name)

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2, color="#5b7cfa")

    h = (b - a) / n

    for i in range(int(n)):
        xi = a + i * h
        ax.bar(xi, f(xi, function_name), width=h, align='edge', alpha=0.3, color="#a6d6ff")

    ax.set_title("График функции и прямоугольники")
    ax.grid(True, alpha=0.3)

    return fig

function_name = st.selectbox(
    "Выберите функцию",
    ["x^2", "sin(x)", "cos(x)", "e^x"]
)

col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("Начало (a)", value=0.0)

with col2:
    b = st.number_input("Конец (b)", value=1.0)

with col3:
    n = st.number_input("Разбиения (n)", value=10)

st.divider()

if st.button("🚀 Вычислить", use_container_width=True):

    h = (b - a) / int(n)

    st.markdown("### 📌 Процесс вычисления")

    st.write(f"h = (b - a) / n = ({b} - {a}) / {int(n)} = {h}")

    sum_result = 0
    steps = []

    for i in range(int(n)):
        x = a + i * h
        fx = f(x, function_name)
        area = fx * h
        sum_result += area

        steps.append(f"i={i}, x={round(x,3)}, f(x)={round(fx,3)}, площадь={round(area,3)}")

    st.markdown("### 📊 Шаги вычисления:")

    for s in steps[:15]:
        st.write(s)

    if int(n) > 15:
        st.write("... (показаны первые 15 шагов)")

    st.markdown("### 📌 Итог:")

    st.markdown(f"""
    <div class="result-box">
    Интеграл ≈ {sum_result}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📈 График")

    fig = plot_graph(a, b, int(n), function_name)
    st.pyplot(fig)

    st.balloons()