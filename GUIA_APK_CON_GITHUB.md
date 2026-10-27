# Hacer el APK con anuncios (sin instalar nada en tu PC)

GitHub compila el APK por ti, gratis, en la nube. Tardas unos 15 minutos la primera vez.

## 1. Subir el proyecto
1. Crea una cuenta en https://github.com y pulsa **New repository** (nombre: `bear-arena`, público o privado).
2. Descomprime este zip. En el repositorio pulsa **uploading an existing file** y arrastra TODO el contenido de la carpeta (incluida la carpeta oculta `.github`; si no se sube, crea el archivo a mano con *Add file → Create new file*, escribe `.github/workflows/android.yml` y pega el contenido).
3. Pulsa **Commit changes**.

## 2. Compilar
1. Pestaña **Actions** → "Build Android APK" → **Run workflow**.
2. Espera 8–12 minutos hasta que salga un check verde.
3. Abre la ejecución → abajo, en **Artifacts**, descarga `bear-arena-apk` → descomprime → `app-debug.apk`.
4. Pásalo a tu móvil e instálalo (permite "instalar apps desconocidas").
Si sale una X roja, entra al paso que falló y mándame el texto del error.

## 3. Probar los anuncios
Esta versión usa anuncios de PRUEBA de Google (siempre funcionan, no dan ingresos). Verás: botón "Duplicar monedas" al terminar una partida, "RECLAMAR x2" en el bono diario, "+100 · anuncio" y el "Pase" en la Tienda.

## 4. Anuncios reales (ingresos)
1. Crea una cuenta en https://admob.google.com → **Aplicaciones → Añadir aplicación** (Android) → copia el **ID de la app** (`ca-app-pub-XXXX~YYYY`).
2. Crea un bloque de anuncios tipo **Con recompensa** → copia su ID (`ca-app-pub-XXXX/ZZZZ`).
3. En GitHub: Settings → Secrets and variables → Actions → pestaña **Variables** → crea `ADMOB_APP_ID` y `ADMOB_REWARDED_ID` con esos valores.
4. Vuelve a ejecutar el workflow. Con `ADMOB_REWARDED_ID` puesto, el juego pasa a anuncios reales.
No pulses tus propios anuncios reales: Google puede suspender tu cuenta.

## 5. Publicar en Google Play (lo que falta)
- Política de privacidad: activa GitHub Pages (Settings → Pages → rama `main`, carpeta `/docs`) y usa `https://TU-USUARIO.github.io/bear-arena/privacy.html` (edita tu correo en `docs/privacy.html`).
- En Play Console declara **"La app contiene anuncios"** y completa Seguridad de los datos (AdMob recopila el ID de publicidad).
- Hace falta un `.aab` firmado, no el APK de pruebas. Cuando llegues aquí te preparo la firma automática.
- Cambia el `appId` en `capacitor.config.json` (`com.tuestudio.beararena`) por el tuyo antes de publicar; no se puede cambiar después.
