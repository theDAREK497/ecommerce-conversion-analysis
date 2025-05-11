import matplotlib.pyplot as plt
import seaborn as sns

def plot_conversion_by_device(df):
    plt.figure(figsize=(8, 6))
    sns.barplot(x='device_type', y='conversion', data=df)
    plt.title('Conversion Rate by Device Type')
    plt.savefig('docs/images/conversion_by_device.png')
    plt.close()

def plot_page_load_vs_bounce(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='page_load_time_seconds', y='bounce_rate', data=df, hue='device_type')
    plt.title('Page Load Time vs Bounce Rate')
    plt.savefig('docs/images/page_load_vs_bounce.png')
    plt.close()