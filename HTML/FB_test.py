from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import bs4
import requests as req

driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)

#計數器數字
num = 52
total = 453

#是否打開計數器
switch = False #輸入True 或 False
mail = 1
time_1 = 0.5
time_2 = 2

#你想輸入的內容
keyword = "哈哈 屁眼"

#你的Facebook帳號
# facebook_gmail = "請輸入帳號@gmail.com"
facebook_gmail = [""]
num_mail = len(facebook_gmail)-1
print(num_mail)


#你的Facebook密碼
# facebook_password = "請輸入密碼"
facebook_password = ""

##文章輸入
X = "Oct 1 2020 – July 31 2021 We study the physics of: A. Quantum entanglement and its robustness B. Quantum algorithm and its development A. Quantum Entanglement and the Measurement of its Robustness We study the behaviors of entangled qubits (Appendix A) on the IBM Rochester with various connectivities and under a “noisy” environment. A phase trajectory analysis based on our measurements of the GHZ-like states is performed. Our results point to an important fact that entangled qubits are “protected” against environmental noise by a scaling property that impacts only the weighting of their amplitudes. Research Approach The reproducibility of most measurements has been confirmed within a reasonably short gate operation time. The two qubits Mermin’s polynomials (n=2) are The expectation values of the Mermin’s polynomials for a 2-qubit are easily derived as shown: Here, we modify the Mermin’s polynomials with measurement method as shown in Eq.(4), and actually carry out measurements on IBM Rochester with and its associated . For a pure GHZ-like state, since , measurements for as opposed to give exactly the same values. However, because of the environmental noise in a NISQ system, there are other possible states besides the initial GHZ-like states, that can be excited before measurement. The excited entangled state can be written as which is a quantum state in the subspace spanned by and , r, a, are parameters that determines the density matrix of . The newly entangled state ρ' can be generated as a result of energy fluctuation, and 3 Therefore, one could not observe noise-excited entanglement states in a NISQ system with the conventional . However, with our modified measurements of and , as shown above, the entangled evolution of noise-excited states in a NISQ system can be easily measured. In other words, and measurements allow the study of phase trajectory portraits of not only the GHZ-like states, but also any noise-induced quantum states. Therefore, the modified and measurements will be used for our phase trajectory analysis throughout. The quantum circuit to create the GHZ state and carry out XY measurements are shown in Fig.1. (a) and (b), respectively. Research Results Figure 2a shows the measurements of and on the IBM Rochester. Figure 2b shows the classical simulation of and for different T1. All 2-qubit pairs on the IBM Rochester were measured. Figure 2a clearly shows that the entangled radii are different for all different 2-qubit pairs, even though they could be of the same phase. Measurement results were then compared with classical simulations involving different T1. From Fig. 2b, it is clear that radii of the circles shrink as the value decreases. To study noise, we introduced parameters to the amplitude of the GHZ-like state and the noise-excited (Supplement A). Considering both and the newly excited on a NISQ computer, measurements of and show different trajectories arising due to the influence of the entanglement strength (characterized by parameter ). Our theoretical analytic results and classical simulations of the influences of are given in Supplement C and D. Quantum measurements on the IBM NISQ computer indeed testifies strongly to our theory of 4 amplitude transition between states, as evident in the significant changes of the circular radii. The superposition amplitude of the GHZ-like states are indeed very sensitive to the environment, but the persistence of the circular trajectories speaks for an important fact, i.e. their entanglement is reasonably robust. In fact, the redistribution of the amplitudes suggests that the noise induces energy transition between states . It is important to note that the circular shapes persist (Fig. 2a) and the sinusoidal waves are all in phase (Fig. 2c). Classical simulations show that the amplitudes of sinusoidal waves will decrease as T1 decreases (Fig. 2c) but no phase shift is induced by any environmental noise. This indicates that entangled qubits are “protected” against environmental noise by a scaling property that impacts only the weighting of their amplitudes (Supplement C). 5 B. Quantum algorithm We have reviewed (see Appendix B) the core concepts of the following major algorithms 1. Quantum Fourier Transformation 2. Grover’s Algorithm 3. Hybrid Quantum-Classical Algorithm 4. Digital Annealing 5. Quantum Error Mitigation Quantum circuits for Quantum Fourier Transformation Quantum circuits for the Grover Algorithm 6 7 Appendix A 8 Appendix B 107年度專題研究計畫"
X = X.split(" ")
print(X[0])
Y = len(X)
print(Y)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
def cl (xp):
    c = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xp))
    )
    c.click()

def ent (xp, word):
    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xp))
    )
    e.clear()
    e.send_keys(word)
driver.get('https://m.facebook.com/login/?locale=zh_TW&refsrc=deprecated')
ent('//*[@id="m_login_email"]',facebook_gmail[mail])
ent('//*[@id="m_login_password"]',facebook_password)
cl('//*[@id="login_password_step_element"]/button')
time.sleep(5)

driver.get('https://fb.watch/jObsah2H3L/')
time.sleep(10)

next = True

while next:

  talk2 = WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="watch_feed"]/div/div[1]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div/div[1]/p'))
  )

  # talk2.send_keys(f'{keyword}{num}')
  talk2.send_keys(f'{X[num]}')

  send = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="focused-state-composer-submit"]/span/div'))
  )
  send.click()
  if num>= Y-1:
    num = 0
  else:
    num = num + 1
    time.sleep(random.uniform(time_1, time_2))
  if total > 1000:
    total = 0
    mail = num_mail - mail
    driver.get('https://fb.watch/jObsah2H3L/')

    login2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/div[1]/a/div[1]/div/span/span'))
    )

    login2.click()

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
    )

    login = driver.find_element(By.NAME,"login")
    username.clear()
    password.clear()
    username.send_keys(facebook_gmail[mail])
    password.send_keys(facebook_password)
    login.click()
  else:
    total = total+1
    print(total)