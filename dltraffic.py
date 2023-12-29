import pandas as pd
import matplotlib.pyplot as plt


data = {
    'region': ['United States', 'China', 'Russia', 'Brazil', 'Germany', 'Canada', 'France', 'United Kingdom', 'Poland', 'Turkey', 'Philippines', 'Ukraine', 'Korea', 'Australia', 'Indonesia', 'Japan'],
    'users': [14.43, 11.64, 9.57, 4.77, 4.16, 3.11, 3.04, 3, 2.6, 2.38, 2.22, 1.96, 1.71, 1.71, 1.62, 1.06],
    'bytes': [286.5, 281.3, 76.8, 52.2, 64, 36.8, 30.7, 42.4, 26, 22.3, 10.7, 16, 27.9, 21.5, 6.9, 26.9]
}

def users():
    df = pd.DataFrame(data)
    df.plot(x='region', y='users', kind='bar', legend=False)
    plt.title('Steam Users rate by Region')
    plt.xlabel('Region')
    plt.ylabel('Users')
    plt.show()

def byte():
    df = pd.DataFrame(data)
    df.plot(x='region', y='users', kind='bar', legend=False)
    plt.title('Steam Total Download Bytes(PB) by region')
    plt.xlabel('Region')
    plt.ylabel('bytes')
    plt.show()

def main():
    users()
    byte()
    df.plot(x='region', y=['users', 'bytes'], kind='bar')
    plt.title('Steam Users and Bytes by Region')
    plt.xlabel('Region')
    lt.ylabel('Users / Bytes')
    plt.show()
    
if __name__ == "__main__":
    main()