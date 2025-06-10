import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset
data = {
    "Garment": ["Shirt", "Shirt", "Pants", "Jacket", "Dress", "Dress", "Pants", "Jacket"],
    "Season": ["Summer", "Winter", "Winter", "Winter", "Summer", "Winter", "Summer", "Summer"],
    "Style": ["Casual", "Formal", "Formal", "Casual", "Formal", "Casual", "Casual", "Formal"],
    "Fabric": ["Cotton", "Flannel", "Wool", "Leather", "Silk", "Velvet", "Linen", "Tweed"]
}
df = pd.DataFrame(data)

# Encode
le_garment = LabelEncoder()
le_season = LabelEncoder()
le_style = LabelEncoder()
le_fabric = LabelEncoder()

df['Garment'] = le_garment.fit_transform(df['Garment'])
df['Season'] = le_season.fit_transform(df['Season'])
df['Style'] = le_style.fit_transform(df['Style'])
df['Fabric'] = le_fabric.fit_transform(df['Fabric'])

X = df[['Garment', 'Season', 'Style']]
y = df['Fabric']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "fabric_model.pkl")
joblib.dump(le_garment, "le_garment.pkl")
joblib.dump(le_season, "le_season.pkl")
joblib.dump(le_style, "le_style.pkl")
joblib.dump(le_fabric, "le_fabric.pkl")
