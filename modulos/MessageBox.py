from PySide6.QtWidgets import QMessageBox

def si_no_mensaje(titulo, mensaje) -> int:
    dlg = QMessageBox()
    dlg.setWindowTitle(titulo)
    dlg.setText(mensaje)
    dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    dlg.setIcon(QMessageBox.Icon.Question)
    return dlg.exec()

def mensaje_simple(titulo, texto) -> None:
    dlg = QMessageBox()
    dlg.setWindowTitle(titulo)
    dlg.setText(texto)
    button = dlg.exec()

    if button == QMessageBox.StandardButton.Ok:
        print("OK!")