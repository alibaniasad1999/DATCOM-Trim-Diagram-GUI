import numpy as np
file = open('export/Trim_diag.out', 'r')
data = []
for line in file:
    temp = list(line.split())
    if '0' in temp:
        temp.remove('0')
    data.append(temp)
file.close()
data = [ele for ele in data if ele != []]
for i in data:
    if 'ALPHA' in i:
        alpha_index = int(i.index('ALPHA'))
        if 'CL' in i:
            cl_index = int(i.index('CL'))
            cm_index = int(i.index('CM'))
            cla_index = int(i.index('CLA'))
            cma_index = int(i.index('CMA'))
            alpha_array = [float(data[int(data.index(i))+1][alpha_index]), float(data[int(data.index(i))+2][alpha_index])]
            cl_array = [float(data[int(data.index(i))+1][cl_index]), float(data[int(data.index(i))+2][cl_index])]
            cm_array = [float(data[int(data.index(i))+1][cm_index]), float(data[int(data.index(i))+2][cm_index])]
            cla_array = [float(data[int(data.index(i))+1][cla_index]), float(data[int(data.index(i))+2][cla_index])]
            cma_array = [float(data[int(data.index(i))+1][cma_index]), float(data[int(data.index(i))+2][cma_index])]
            if alpha_array[1] > alpha_array[0]:
                c_m_zero_data = cm_array[0]
                c_l_zero_data = cl_array[0]
                c_l_alpha_data = cla_array[1]
                c_m_alpha_data = cma_array[1]
            else:
                c_m_zero_data = cm_array[1]
                c_l_zero_data = cl_array[2]
                c_l_alpha_data = cla_array[2]
                c_m_alpha_data = cma_array[2]
            break

for i in data:
    if ('DELTA' and 'D(CL)') in i:
        elevator_datcom_data = data[int(data.index(i)) : int(data.index(i)) + 10]

elevator_deflection_index = int(elevator_datcom_data[0].index('DELTA'))
elevator_delta_cl_index = int(elevator_datcom_data[0].index('D(CL)'))
elevator_delta_cm_index = int(elevator_datcom_data[0].index('D(CM)'))
elevator_deflection_array = []
elevator_delta_cl_array = []
elevator_delta_cm_array = []
for i in elevator_datcom_data[1:]:
    elevator_deflection_array.append(float(i[elevator_deflection_index]))
    elevator_delta_cl_array.append(float(i[elevator_delta_cl_index]))
    elevator_delta_cm_array.append(float(i[elevator_delta_cm_index]))

x = np.array(elevator_deflection_array)
y = np.array(elevator_delta_cl_array)

p_cl = np.polyfit(x, y, 1)

x = np.array(elevator_deflection_array)
y = np.array(elevator_delta_cm_array)

p_cm = np.polyfit(x, y, 1)


print('done')