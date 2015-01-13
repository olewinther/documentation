# Learn about API authentication here: {{BASE_URL}}/python/getting-started
# Find your api_key here: {{BASE_URL}}/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('TestBot', 'r1neazxo9w')
trace1 = Contour(
    z=[[1.5, 1.2346938775510206, 1.010204081632653, 0.8265306122448979, 0.6836734693877551, 0.5816326530612246, 0.5204081632653061, 0.5, 0.5204081632653061, 0.5816326530612244, 0.683673469387755, 0.8265306122448979, 1.010204081632653, 1.2346938775510201, 1.5], [1.3673469387755102, 1.102040816326531, 0.8775510204081634, 0.6938775510204083, 0.5510204081632655, 0.4489795918367348, 0.3877551020408164, 0.3673469387755103, 0.38775510204081637, 0.4489795918367347, 0.5510204081632653, 0.6938775510204083, 0.8775510204081632, 1.1020408163265305, 1.3673469387755102], [1.2551020408163265, 0.989795918367347, 0.7653061224489797, 0.5816326530612245, 0.4387755102040817, 0.33673469387755106, 0.2755102040816327, 0.25510204081632654, 0.2755102040816326, 0.33673469387755095, 0.43877551020408145, 0.5816326530612245, 0.7653061224489794, 0.9897959183673466, 1.2551020408163265], [1.163265306122449, 0.8979591836734695, 0.673469387755102, 0.4897959183673469, 0.34693877551020413, 0.24489795918367352, 0.1836734693877551, 0.16326530612244897, 0.18367346938775508, 0.24489795918367338, 0.3469387755102039, 0.4897959183673469, 0.6734693877551019, 0.897959183673469, 1.163265306122449], [1.0918367346938775, 0.8265306122448981, 0.6020408163265306, 0.41836734693877553, 0.27551020408163274, 0.17346938775510212, 0.1122448979591837, 0.09183673469387757, 0.11224489795918367, 0.17346938775510198, 0.2755102040816325, 0.41836734693877553, 0.6020408163265305, 0.8265306122448977, 1.0918367346938775], [1.0408163265306123, 0.7755102040816328, 0.5510204081632654, 0.3673469387755102, 0.2244897959183674, 0.12244897959183682, 0.06122448979591841, 0.04081632653061227, 0.06122448979591837, 0.12244897959183668, 0.2244897959183672, 0.3673469387755102, 0.5510204081632653, 0.7755102040816324, 1.0408163265306123], [1.010204081632653, 0.7448979591836736, 0.5204081632653061, 0.336734693877551, 0.1938775510204082, 0.09183673469387761, 0.030612244897959204, 0.010204081632653067, 0.03061224489795917, 0.09183673469387749, 0.19387755102040802, 0.336734693877551, 0.520408163265306, 0.7448979591836732, 1.010204081632653], [1.0, 0.7346938775510206, 0.5102040816326531, 0.32653061224489793, 0.18367346938775514, 0.08163265306122454, 0.020408163265306135, 0.0, 0.020408163265306103, 0.08163265306122441, 0.18367346938775495, 0.32653061224489793, 0.510204081632653, 0.7346938775510201, 1.0], [1.010204081632653, 0.7448979591836736, 0.5204081632653061, 0.336734693877551, 0.19387755102040818, 0.0918367346938776, 0.030612244897959186, 0.010204081632653052, 0.030612244897959155, 0.09183673469387746, 0.193877551020408, 0.336734693877551, 0.520408163265306, 0.7448979591836732, 1.010204081632653], [1.0408163265306123, 0.7755102040816327, 0.5510204081632653, 0.36734693877551017, 0.22448979591836735, 0.12244897959183675, 0.06122448979591834, 0.04081632653061221, 0.06122448979591831, 0.12244897959183662, 0.22448979591836715, 0.36734693877551017, 0.5510204081632651, 0.7755102040816323, 1.0408163265306123], [1.0918367346938775, 0.826530612244898, 0.6020408163265305, 0.4183673469387754, 0.2755102040816326, 0.173469387755102, 0.1122448979591836, 0.09183673469387747, 0.11224489795918358, 0.1734693877551019, 0.2755102040816324, 0.4183673469387754, 0.6020408163265304, 0.8265306122448975, 1.0918367346938775], [1.163265306122449, 0.8979591836734695, 0.673469387755102, 0.4897959183673469, 0.34693877551020413, 0.24489795918367352, 0.1836734693877551, 0.16326530612244897, 0.18367346938775508, 0.24489795918367338, 0.3469387755102039, 0.4897959183673469, 0.6734693877551019, 0.897959183673469, 1.163265306122449], [1.2551020408163265, 0.989795918367347, 0.7653061224489796, 0.5816326530612244, 0.4387755102040816, 0.336734693877551, 0.2755102040816326, 0.2551020408163265, 0.27551020408163257, 0.3367346938775509, 0.43877551020408145, 0.5816326530612244, 0.7653061224489794, 0.9897959183673466, 1.2551020408163265], [1.3673469387755102, 1.1020408163265305, 0.8775510204081631, 0.693877551020408, 0.5510204081632653, 0.4489795918367346, 0.3877551020408162, 0.36734693877551006, 0.38775510204081615, 0.44897959183673447, 0.551020408163265, 0.693877551020408, 0.877551020408163, 1.10204081632653, 1.3673469387755102], [1.5, 1.2346938775510206, 1.010204081632653, 0.8265306122448979, 0.6836734693877551, 0.5816326530612246, 0.5204081632653061, 0.5, 0.5204081632653061, 0.5816326530612244, 0.683673469387755, 0.8265306122448979, 1.010204081632653, 1.2346938775510201, 1.5]],
    x=[-1.0, -0.8571428571428572, -0.7142857142857143, -0.5714285714285714, -0.4285714285714286, -0.2857142857142858, -0.1428571428571429, 0.0, 0.1428571428571428, 0.2857142857142856, 0.4285714285714284, 0.5714285714285714, 0.7142857142857142, 0.857142857142857, 1.0],
    y=[-1.0, -0.8571428571428572, -0.7142857142857143, -0.5714285714285714, -0.4285714285714286, -0.2857142857142858, -0.1428571428571429, 0.0, 0.1428571428571428, 0.2857142857142856, 0.4285714285714284, 0.5714285714285714, 0.7142857142857142, 0.857142857142857, 1.0],
    ncontours=30,
    showscale=False
)
trace2 = Scatter(
    x=[-0.8, -0.48, -0.288, -0.17279999999999998, -0.10367999999999998, -0.062207999999999986, -0.03732479999999999, -0.022394879999999992, -0.013436927999999996, -0.008062156799999998, -0.004837294079999999, -0.002902376447999999, -0.0017414258687999994, -0.0010448555212799996, -0.0006269133127679996, -0.0003761479876607998],
    y=[-0.9, -0.72, -0.576, -0.4608, -0.36863999999999997, -0.29491199999999995, -0.23592959999999996, -0.18874367999999997, -0.15099494399999996, -0.12079595519999997, -0.09663676415999997, -0.07730941132799998, -0.061847529062399986, -0.04947802324991999, -0.03958241859993599, -0.031665934879948794],
    mode='markers+lines',
    name='steepest',
    line=Line(
        color='black'
    )
)
data = Data([trace1, trace2])
plot_url = py.plot(data, filename='contour-scatter', auto_open=False)
