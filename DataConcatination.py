import pandas as pd

df1 = pd.read_csv('AnalyzedReviewsBatoul.csv')
df2 = pd.read_csv('AnalyzedReviewsSamira.csv')
df3 = pd.read_csv('AnalyzedReviewsMhmd.csv')

combined = pd.concat([df1, df2, df3],axis=1)
combined.to_csv('analyzed_reviews_with_id.csv', index=False)
