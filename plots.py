import matplotlib.pyplot as plt

n_values = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
alg1_empirical_rt = [8573.37, 50384.34, 106307.94, 178263.26, 302628.04, 384481.31, 612900.62, 866122.62, 1007012.71, 1416751.78]
alg2_empirical_rt = [24.19, 66.89, 110.07, 165.46, 184.05, 216.47, 241.74, 285.22, 290.43, 300.07]
alg1_predicted_rt = [14168, 56672, 127512, 226688, 354200, 510048, 694232, 906752, 1147608, 1416800]
alg2_predicted_rt = [35.84897,77.10229,120.45727,165.26132,210.72794,257.04132,304.36926,353.84309,402.67346,454.07633]

plt.figure(figsize=(10, 6))
plt.plot(n_values, alg1_empirical_rt, marker='o', label='ALG1 Empirical RT', color = 'red')
plt.plot(n_values, alg2_empirical_rt, marker='o', label='ALG2 Empirical RT',color = 'blue')
plt.xlabel('n')
plt.ylabel('Empirical RT')
plt.title('ALG1 and ALG2 Empirical RT')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(n_values, alg1_empirical_rt, marker='o', label='ALG1 Empirical RT',color = 'green')
plt.plot(n_values, alg1_predicted_rt, marker='o', label='ALG1 Predicted RT',color = 'black')
plt.xlabel('n')
plt.ylabel('RT')
plt.title('ALG1 Empirical RT vs Predicted RT')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(n_values, alg2_empirical_rt, marker='o', label='ALG2 Empirical RT',color = 'orange')
plt.plot(n_values, alg2_predicted_rt, marker='o', label='ALG2 Predicted RT',color = 'purple')
plt.xlabel('n')
plt.ylabel('RT')
plt.title('ALG2 Empirical RT vs Predicted RT')
plt.legend()
plt.show()
