"""Function to normalize the data model"""

def create_dim_dataframe(df, dim_columns, id_column, return_original=True):
    # Create a new DataFrame with the specified dimension columns
    df_dim = df[dim_columns].drop_duplicates().reset_index(drop=True)
    df_dim[id_column] = df_dim.index + 1

    # put id column first
    df_dim = df_dim[[id_column] + dim_columns]

    if return_original:
        # add new id column
        df = df.merge(df_dim, on=dim_columns, how='left')
        return df_dim, df
    return df_dim
