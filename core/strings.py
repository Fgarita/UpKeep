# -*- coding: utf-8 -*-
"""
All translatable text for the app: static UI chrome, category names,
task titles/descriptions/confirmations, and the live-log messages each
task prints while it runs.

Keys are plain strings shared by both languages so the rest of the app
never has to know which language is active — it just calls t(key).
"""

STRINGS = {
    "en": {
        # --- Window / navigation ---
        "app.title": "PC Maintenance",
        "nav.exit": "Exit",

        # --- Categories ---
        "category.home": "Home",
        "category.cleanup": "Cleanup",
        "category.system": "System",
        "category.network_performance": "Network & Performance",
        "category.updates": "Updates",
        "category.diagnostics": "Diagnostics",
        "category.external_tools": "External Tools",

        # --- Home page ---
        "home.title": "PC Maintenance",
        "home.subtitle": "Choose which tasks to run in automatic mode and press "
                          "Run. You can uncheck anything you don't want to do now.",

        # --- Buttons ---
        "button.run": "Run",
        "button.run_only_this": "Run only this",
        "button.run_selected": "Run selected",
        "button.select_all": "Select all",
        "button.deselect_all": "Deselect all",

        # --- Live console ---
        "console.live_log": "Live log",
        "console.idle": "Idle",
        "console.running": "Running: {title}",
        "console.done": "Done",
        "console.ok": "OK",
        "console.error": "ERROR",

        # --- Dialogs / notifications ---
        "confirm.title": "Confirm",
        "infobar.nothing_selected.title": "Nothing selected",
        "infobar.nothing_selected.content": "Select at least one task.",
        "infobar.busy.title": "Tasks already running",
        "infobar.busy.content": "Wait for the current maintenance run to finish.",
        "worker.error": "[!] Error in '{title}': {error}",

        # --- Tasks: cleanup ---
        "task.restore_point.title": "Restore point",
        "task.restore_point.description": "Creates a restore point before touching anything.",
        "task.close_browsers.title": "Close browsers",
        "task.close_browsers.description": "Closes Chrome, Edge, Firefox and Brave.",
        "task.browser_cache.title": "Browser cache",
        "task.browser_cache.description": "Clears the Chrome, Edge and Firefox cache.",
        "task.temp_files.title": "Temporary files",
        "task.temp_files.description": "Deletes TEMP, Windows\\Temp and Prefetch.",
        "task.recycle_bin.title": "Recycle Bin",
        "task.recycle_bin.description": "Empties the Recycle Bin.",
        "task.update_cache.title": "Windows Update cache",
        "task.update_cache.description": "Clears SoftwareDistribution\\Download.",
        "task.font_cache.title": "Font cache",
        "task.font_cache.description": "Rebuilds the Windows font cache.",
        "task.store_reset.title": "Microsoft Store cache",
        "task.store_reset.description": "Resets the Microsoft Store cache.",
        "task.disk_cleanup.title": "Disk Cleanup",
        "task.disk_cleanup.description": "Runs the Windows Disk Cleanup tool.",
        "task.winsxs.title": "Old components (WinSxS)",
        "task.winsxs.description": "Cleans up old Windows components.",

        # --- Tasks: system ---
        "task.repair_files.title": "Repair system files",
        "task.repair_files.description": "Runs SFC and DISM RestoreHealth.",
        "task.check_disk.title": "Check disk errors",
        "task.check_disk.description": "chkdsk C: /scan, no restart.",
        "task.telemetry.title": "Disable telemetry",
        "task.telemetry.description": "Disables telemetry scheduled tasks.",
        "task.pending_reboot.title": "Pending reboot",
        "task.pending_reboot.description": "Checks whether Windows needs a restart.",

        # --- Tasks: network & performance ---
        "task.network_reset.title": "Reset DNS & network",
        "task.network_reset.description": "flushdns + reset winsock/TCP-IP/firewall.",
        "task.active_adapter.title": "Active network adapter",
        "task.active_adapter.description": "Renews the IP only on the adapter in use.",
        "task.optimize_drives.title": "Optimize drives",
        "task.optimize_drives.description": "Defrag on HDD / TRIM on SSD.",
        "task.performance.title": "High performance mode",
        "task.performance.description": "Switches the power plan and restarts Explorer.",
        "task.speed_test.title": "Speed test",
        "task.speed_test.description": "Measures approximate download speed.",
        "task.cpu_processes.title": "Processes by CPU",
        "task.cpu_processes.description": "Lists the processes using the most CPU.",

        # --- Tasks: updates ---
        "task.update_apps.title": "Update applications",
        "task.update_apps.description": "winget upgrade --all.",
        "task.update_windows.title": "Update Windows",
        "task.update_windows.description": "Installs pending Windows updates.",
        "task.drivers.title": "Check drivers",
        "task.drivers.description": "Opens Windows Update to check for drivers.",

        # --- Tasks: diagnostics ---
        "task.disk_space.title": "Disk space",
        "task.disk_space.description": "Free space report per drive.",
        "task.defender_scan.title": "Defender scan",
        "task.defender_scan.description": "Windows Defender quick scan.",
        "task.smart.title": "Disk health (SMART)",
        "task.smart.description": "SMART status of the physical disks.",
        "task.recent_events.title": "Recent events",
        "task.recent_events.description": "Latest 20 system errors/warnings.",
        "task.clear_logs.title": "Clear Event Viewer",
        "task.clear_logs.description": "Erases the Windows event log history.",
        "task.clear_logs.confirm": "This erases the HISTORY of all Event Viewer logs "
                                    "(Application, System, Security, etc). It does not delete "
                                    "files or programs, only the recorded event history.\n\nContinue?",

        # --- Tasks: external tools ---
        "task.debloat.title": "Win11Debloat",
        "task.debloat.description": "Third-party tool to remove bloatware and ads.",
        "task.debloat.confirm": "Win11Debloat (github.com/Raphire/Win11Debloat) is an open-source "
                                 "project, not made by Anthropic. It will open its own interactive "
                                 "menu, where you decide every change.\n\nOpen Win11Debloat?",

        # --- Live-log messages (op.<task_id>.<message>) ---
        "op.restore_point.start": "Creating a system restore point...",
        "op.restore_point.done": "Restore point created (if System Protection is enabled on C:).",

        "op.close_browsers.start": "Closing browsers...",
        "op.close_browsers.done": "Browsers closed.",

        "op.network_reset.start": "Flushing DNS and resetting network...",
        "op.network_reset.done": "Network reset. A restart is recommended afterwards.",

        "op.browser_cache.start": "Clearing browser cache...",
        "op.browser_cache.done": "Browser cache cleared.",

        "op.temp_files.start": "Deleting temporary files...",
        "op.temp_files.done": "Temporary files deleted.",

        "op.recycle_bin.start": "Emptying the Recycle Bin...",
        "op.recycle_bin.done": "Recycle Bin emptied.",

        "op.update_cache.start": "Clearing Windows Update cache...",
        "op.update_cache.done": "Windows Update cache cleared.",

        "op.disk_cleanup.start": "Running Disk Cleanup...",
        "op.disk_cleanup.done": "Disk cleanup completed.",

        "op.repair_files.start": "Checking system file integrity (this can take several minutes)...",
        "op.repair_files.done": "System file check completed.",

        "op.telemetry.start": "Disabling telemetry scheduled tasks...",
        "op.telemetry.done": "Telemetry scheduled tasks disabled.",

        "op.optimize_drives.start": "Optimizing drives (defrag on HDD / TRIM on SSD)...",
        "op.optimize_drives.done": "Drive optimization completed.",

        "op.update_apps.start": "Checking for application updates...",
        "op.update_apps.missing": 'winget is not available. Install it from the Microsoft Store ("App Installer").',

        "op.update_windows.start": "Checking for Windows updates...",
        "op.update_windows.done": "Windows Update processed. If it didn't run automatically, check Settings > Windows Update.",

        "op.drivers.start": "Opening Windows Update to check for drivers...",
        "op.drivers.done": "You can also check Device Manager (devmgmt.msc).",

        "op.performance.start": "Applying performance optimizations...",
        "op.performance.top_ram": "Top processes by RAM:\n{table}",
        "op.performance.done": "Power plan switched to High Performance.",

        "op.disk_space.start": "Generating disk space report...",
        "op.disk_space.failed": "Could not generate the report.",

        "op.defender_scan.start": "Running a Windows Defender quick scan (this can take several minutes)...",
        "op.defender_scan.done": "Quick scan completed. Check the Windows Security Center if it found threats.",
        "op.defender_scan.missing": "MpCmdRun.exe was not found. If you use another antivirus, scan from that app.",

        "op.smart.start": "Checking disk health (SMART)...",
        "op.smart.failed": "Could not read SMART status.",
        "op.smart.note": "If the status isn't OK/Healthy, back up your data as soon as possible.",

        "op.pending_reboot.start": "Checking whether a reboot is pending...",
        "op.pending_reboot.yes": "A reboot is pending.",
        "op.pending_reboot.no": "No reboot is pending.",

        "op.font_cache.start": "Clearing the Windows font cache...",
        "op.font_cache.done": "Font cache cleared.",

        "op.clear_logs.start": "Clearing Event Viewer logs...",
        "op.clear_logs.done": "Event Viewer logs cleared.",

        "op.speed_test.start": "Testing internet speed...",
        "op.speed_test.fallback": "speedtest-cli is not installed, falling back to a download test...",
        "op.speed_test.result": "Approximate download speed: {mbps} Mbps",
        "op.speed_test.failed": "Could not complete the speed test (check your connection).",

        "op.active_adapter.start": "Looking for active network adapters...",
        "op.active_adapter.renewing": "Renewing IP on the active adapter: {name}",
        "op.active_adapter.done": "IP renewed on {name}.",
        "op.active_adapter.none": "No active adapter was detected.",

        "op.check_disk.start": "Checking for disk errors (online scan, no restart)...",
        "op.check_disk.done": "Disk check completed. If it suggests /f, run it manually: chkdsk C: /f /r",

        "op.store_reset.start": "Resetting the Microsoft Store cache...",
        "op.store_reset.done": "Microsoft Store cache reset.",

        "op.winsxs.start": "Cleaning up old Windows components (WinSxS)... this can take several minutes.",
        "op.winsxs.done": "Component cleanup completed.",

        "op.recent_events.system_start": "Reading the latest System events (errors/warnings)...",
        "op.recent_events.system_empty": "No recent System events.",
        "op.recent_events.app_start": "Reading the latest Application events (errors/warnings)...",
        "op.recent_events.app_empty": "No recent Application events.",

        "op.cpu_processes.start": "Reading the processes using the most CPU...",
        "op.cpu_processes.failed": "Could not read the process list.",

        "op.debloat.start": "Opening Win11Debloat (third-party tool, not made by Anthropic)...",
        "op.debloat.done": "Win11Debloat closed.",
    },

    "es": {
        # --- Ventana / navegacion ---
        "app.title": "Mantenimiento de PC",
        "nav.exit": "Salir",

        # --- Categorias ---
        "category.home": "Inicio",
        "category.cleanup": "Limpieza",
        "category.system": "Sistema",
        "category.network_performance": "Red y rendimiento",
        "category.updates": "Actualizaciones",
        "category.diagnostics": "Diagnostico",
        "category.external_tools": "Herramientas externas",

        # --- Pagina de inicio ---
        "home.title": "Mantenimiento de PC",
        "home.subtitle": "Elegi que tareas correr en el modo automatico y presiona "
                          "Ejecutar. Podes desmarcar lo que no quieras hacer ahora.",

        # --- Botones ---
        "button.run": "Ejecutar",
        "button.run_only_this": "Solo esta",
        "button.run_selected": "Ejecutar seleccionadas",
        "button.select_all": "Marcar todas",
        "button.deselect_all": "Desmarcar todas",

        # --- Consola en vivo ---
        "console.live_log": "Registro en vivo",
        "console.idle": "Inactivo",
        "console.running": "Ejecutando: {title}",
        "console.done": "Listo",
        "console.ok": "OK",
        "console.error": "ERROR",

        # --- Dialogos / notificaciones ---
        "confirm.title": "Confirmar",
        "infobar.nothing_selected.title": "Nada seleccionado",
        "infobar.nothing_selected.content": "Marca al menos una tarea.",
        "infobar.busy.title": "Ya hay tareas en curso",
        "infobar.busy.content": "Espera a que termine el mantenimiento actual.",
        "worker.error": "[!] Error en '{title}': {error}",

        # --- Tareas: limpieza ---
        "task.restore_point.title": "Punto de restauracion",
        "task.restore_point.description": "Crea un punto de restauracion antes de tocar nada.",
        "task.close_browsers.title": "Cerrar navegadores",
        "task.close_browsers.description": "Cierra Chrome, Edge, Firefox y Brave.",
        "task.browser_cache.title": "Cache de navegadores",
        "task.browser_cache.description": "Borra la cache de Chrome, Edge y Firefox.",
        "task.temp_files.title": "Archivos temporales",
        "task.temp_files.description": "Elimina TEMP, Windows\\Temp y Prefetch.",
        "task.recycle_bin.title": "Papelera de reciclaje",
        "task.recycle_bin.description": "Vacia la papelera de reciclaje.",
        "task.update_cache.title": "Cache de Windows Update",
        "task.update_cache.description": "Limpia SoftwareDistribution\\Download.",
        "task.font_cache.title": "Cache de fuentes",
        "task.font_cache.description": "Reconstruye la cache de fuentes de Windows.",
        "task.store_reset.title": "Cache de Microsoft Store",
        "task.store_reset.description": "Resetea la cache de la Microsoft Store.",
        "task.disk_cleanup.title": "Liberador de espacio",
        "task.disk_cleanup.description": "Corre el Liberador de espacio en disco.",
        "task.winsxs.title": "Componentes viejos (WinSxS)",
        "task.winsxs.description": "Limpia componentes antiguos de Windows.",

        # --- Tareas: sistema ---
        "task.repair_files.title": "Reparar archivos de sistema",
        "task.repair_files.description": "Corre SFC y DISM RestoreHealth.",
        "task.check_disk.title": "Revisar errores de disco",
        "task.check_disk.description": "chkdsk C: /scan, sin reiniciar.",
        "task.telemetry.title": "Desactivar telemetria",
        "task.telemetry.description": "Deshabilita tareas programadas de telemetria.",
        "task.pending_reboot.title": "Reinicio pendiente",
        "task.pending_reboot.description": "Revisa si Windows necesita un reinicio.",

        # --- Tareas: red y rendimiento ---
        "task.network_reset.title": "Limpiar DNS y red",
        "task.network_reset.description": "flushdns + reset de winsock/TCP-IP/firewall.",
        "task.active_adapter.title": "Adaptador de red activo",
        "task.active_adapter.description": "Renueva la IP solo del adaptador en uso.",
        "task.optimize_drives.title": "Optimizar unidades",
        "task.optimize_drives.description": "Defrag en HDD / TRIM en SSD.",
        "task.performance.title": "Modo alto rendimiento",
        "task.performance.description": "Cambia el plan de energia y reinicia el explorador.",
        "task.speed_test.title": "Test de velocidad",
        "task.speed_test.description": "Mide la velocidad de descarga aproximada.",
        "task.cpu_processes.title": "Procesos por CPU",
        "task.cpu_processes.description": "Lista los procesos que mas CPU consumen.",

        # --- Tareas: actualizaciones ---
        "task.update_apps.title": "Actualizar aplicaciones",
        "task.update_apps.description": "winget upgrade --all.",
        "task.update_windows.title": "Actualizar Windows",
        "task.update_windows.description": "Instala actualizaciones pendientes de Windows.",
        "task.drivers.title": "Revisar drivers",
        "task.drivers.description": "Abre Windows Update para revisar drivers.",

        # --- Tareas: diagnostico ---
        "task.disk_space.title": "Espacio en disco",
        "task.disk_space.description": "Reporte de espacio libre por unidad.",
        "task.defender_scan.title": "Escaneo de Defender",
        "task.defender_scan.description": "Escaneo rapido de Windows Defender.",
        "task.smart.title": "Salud del disco (SMART)",
        "task.smart.description": "Estado SMART de los discos fisicos.",
        "task.recent_events.title": "Eventos recientes",
        "task.recent_events.description": "Ultimos 20 errores/advertencias del sistema.",
        "task.clear_logs.title": "Limpiar Visor de Eventos",
        "task.clear_logs.description": "Borra el historial de logs de Windows.",
        "task.clear_logs.confirm": "Esto borra el HISTORIAL de todos los registros del Visor de Eventos "
                                    "(Aplicacion, Sistema, Seguridad, etc). No borra archivos ni programas, "
                                    "solo el historial de eventos registrados.\n\n¿Continuar?",

        # --- Tareas: herramientas externas ---
        "task.debloat.title": "Win11Debloat",
        "task.debloat.description": "Herramienta externa de terceros para quitar apps y publicidad.",
        "task.debloat.confirm": "Win11Debloat (github.com/Raphire/Win11Debloat) es un proyecto de codigo "
                                 "abierto, no es de Anthropic. Se abrira su propio menu interactivo, donde "
                                 "vos decidis cada cambio.\n\n¿Abrir Win11Debloat?",

        # --- Mensajes de la consola en vivo (op.<task_id>.<mensaje>) ---
        "op.restore_point.start": "Creando punto de restauracion del sistema...",
        "op.restore_point.done": "Punto de restauracion creado (si System Protection esta activado en C:).",

        "op.close_browsers.start": "Cerrando navegadores...",
        "op.close_browsers.done": "Navegadores cerrados.",

        "op.network_reset.start": "Limpiando DNS y reseteando red...",
        "op.network_reset.done": "Red reseteada. Se recomienda reiniciar la PC despues.",

        "op.browser_cache.start": "Limpiando cache de navegadores...",
        "op.browser_cache.done": "Cache de navegadores eliminado.",

        "op.temp_files.start": "Eliminando archivos temporales...",
        "op.temp_files.done": "Archivos temporales eliminados.",

        "op.recycle_bin.start": "Vaciando papelera de reciclaje...",
        "op.recycle_bin.done": "Papelera vaciada.",

        "op.update_cache.start": "Limpiando cache de Windows Update...",
        "op.update_cache.done": "Cache de Windows Update limpiado.",

        "op.disk_cleanup.start": "Ejecutando Liberador de espacio en disco...",
        "op.disk_cleanup.done": "Limpieza de disco completada.",

        "op.repair_files.start": "Verificando integridad del sistema (puede tardar varios minutos)...",
        "op.repair_files.done": "Verificacion de sistema completada.",

        "op.telemetry.start": "Deshabilitando tareas programadas de telemetria...",
        "op.telemetry.done": "Tareas de telemetria deshabilitadas.",

        "op.optimize_drives.start": "Optimizando unidades de disco (defrag en HDD / TRIM en SSD)...",
        "op.optimize_drives.done": "Optimizacion de unidades completada.",

        "op.update_apps.start": "Buscando actualizaciones de aplicaciones instaladas...",
        "op.update_apps.missing": 'winget no esta disponible. Instalalo desde la Microsoft Store ("App Installer").',

        "op.update_windows.start": "Buscando actualizaciones de Windows...",
        "op.update_windows.done": "Windows Update procesado. Si no corrio solo, revisa Configuracion > Windows Update.",

        "op.drivers.start": "Abriendo Windows Update para revisar drivers...",
        "op.drivers.done": "Tambien podes revisar el Administrador de dispositivos (devmgmt.msc).",

        "op.performance.start": "Aplicando optimizaciones de rendimiento...",
        "op.performance.top_ram": "Top procesos por RAM:\n{table}",
        "op.performance.done": "Plan de energia cambiado a Alto Rendimiento.",

        "op.disk_space.start": "Generando reporte de espacio en disco...",
        "op.disk_space.failed": "No se pudo generar el reporte.",

        "op.defender_scan.start": "Ejecutando escaneo rapido de Windows Defender (puede tardar varios minutos)...",
        "op.defender_scan.done": "Escaneo rapido completado. Revisa el Centro de Seguridad si encontro amenazas.",
        "op.defender_scan.missing": "No se encontro MpCmdRun.exe. Si usas otro antivirus, escanea desde esa app.",

        "op.smart.start": "Verificando salud de los discos (SMART)...",
        "op.smart.failed": "No se pudo leer el estado SMART.",
        "op.smart.note": "Si el estado no dice OK/Healthy, respalda tus datos cuanto antes.",

        "op.pending_reboot.start": "Verificando si hay un reinicio pendiente...",
        "op.pending_reboot.yes": "Hay un reinicio pendiente.",
        "op.pending_reboot.no": "No hay reinicios pendientes.",

        "op.font_cache.start": "Vaciando cache de fuentes de Windows...",
        "op.font_cache.done": "Cache de fuentes eliminada.",

        "op.clear_logs.start": "Limpiando logs del Visor de Eventos...",
        "op.clear_logs.done": "Logs del Visor de Eventos limpiados.",

        "op.speed_test.start": "Probando velocidad de internet...",
        "op.speed_test.fallback": "speedtest-cli no esta instalado, usando prueba de descarga alternativa...",
        "op.speed_test.result": "Velocidad de descarga aproximada: {mbps} Mbps",
        "op.speed_test.failed": "No se pudo completar la prueba de velocidad (revisa tu conexion).",

        "op.active_adapter.start": "Buscando adaptadores de red activos...",
        "op.active_adapter.renewing": "Renovando IP en el adaptador activo: {name}",
        "op.active_adapter.done": "IP renovada en {name}.",
        "op.active_adapter.none": "No se detecto un adaptador activo.",

        "op.check_disk.start": "Revisando errores de disco (escaneo en linea, sin reiniciar)...",
        "op.check_disk.done": "Revision de disco completada. Si sugiere /f, correlo manualmente: chkdsk C: /f /r",

        "op.store_reset.start": "Reseteando cache de Microsoft Store...",
        "op.store_reset.done": "Cache de Microsoft Store reseteada.",

        "op.winsxs.start": "Limpiando componentes viejos de Windows (WinSxS)... puede tardar varios minutos.",
        "op.winsxs.done": "Limpieza de componentes completada.",

        "op.recent_events.system_start": "Leyendo ultimos eventos del Sistema (errores/advertencias)...",
        "op.recent_events.system_empty": "Sin eventos recientes de Sistema.",
        "op.recent_events.app_start": "Leyendo ultimos eventos de Aplicacion (errores/advertencias)...",
        "op.recent_events.app_empty": "Sin eventos recientes de Aplicacion.",

        "op.cpu_processes.start": "Leyendo procesos que mas CPU consumen...",
        "op.cpu_processes.failed": "No se pudo leer la lista de procesos.",

        "op.debloat.start": "Abriendo Win11Debloat (herramienta externa, no es de Anthropic)...",
        "op.debloat.done": "Win11Debloat cerrado.",
    },
}
