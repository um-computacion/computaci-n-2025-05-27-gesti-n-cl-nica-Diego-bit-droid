import unittest
from excepciones import TurnoOcupadoException, PacienteNoEncontradoExcepcion

class TestExcepciones(unittest.TestCase):
    def test_turno_ocupado_exception(self):
        with self.assertRaises(TurnoOcupadoException) as context:
            raise TurnoOcupadoException("Turno ya ocupado.")
        self.assertEqual(str(context.exception), "Turno ya ocupado.")

    def test_paciente_no_encontrado_exception(self):
        with self.assertRaises(PacienteNoEncontradoExcepcion) as context:
            raise PacienteNoEncontradoExcepcion("No se ha encontrado al paciente.")
        self.assertEqual(str(context.exception), "No se ha encontrado al paciente.")

if __name__ == "__main__":
    unittest.main()