import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def top_k_hist(df, columns=None, k=10, combine_others=True):
    """
    Display histograms for the top k most frequent values in specified columns.
    """
    df = df.copy()
    if not columns:
        columns = df.select_dtypes(object).columns


    
    for i, c in enumerate(columns):
        # display countplot with only top k values and combine the rest as "Other"
        fig, ax = plt.subplots(figsize=(10, 5))
        top_k = df[c].value_counts().head(k-1) 
        plot_order = top_k.index.tolist()

        # combine columns outside of top k as "Other"
        if len(top_k) < k - 1 and combine_others:
            df[c] = df[c].map(lambda x: "Other" if x not in top_k.index else x)

            plot_order = plot_order + ["Other"]
        
        sns.countplot(df, y=c, order=plot_order, ax=ax)
        plt.title(f"Distribution of column '{c}'")
        plt.ylabel("")
        plt.show()
        
