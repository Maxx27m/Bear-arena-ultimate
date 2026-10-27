import os
p='android/app/src/main/AndroidManifest.xml'
s=open(p,encoding='utf8').read()
app=os.environ.get('ADMOB_APP_ID') or 'ca-app-pub-3940256099942544~3347511713'  # ID de PRUEBA de Google
if 'gms.ads.APPLICATION_ID' not in s:
    s=s.replace('</application>','<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="%s"/></application>'%app)
if 'permission.AD_ID' not in s:
    s=s.replace('<application','<uses-permission android:name="com.google.android.gms.permission.AD_ID"/><application',1)
if 'screenOrientation' not in s:
    s=s.replace('<activity ','<activity android:screenOrientation="sensorLandscape" ',1)
open(p,'w',encoding='utf8').write(s)
print('Manifest listo')
