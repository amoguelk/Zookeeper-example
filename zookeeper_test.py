import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    # -------- MIS PRUEBAS ----------

    def test_creaEphemeral(self):
        tree = Ztree()
        tree.create('/enode','datos',True,True,5,'/')
        nodo = tree.tree.get_node('/enode').data
        self.assertTrue(nodo.ephemeral)
    
    def test_borrar(self):
        tree = Ztree()
        tree.create('/n','contenido',False,True,0,'/')
        tree.delete('/n',0)
        self.assertFalse(tree.exist('/n'))
    
    def test_versionIncorrecta(self):
        tree = Ztree()
        tree.create('/n','contenido',False,True,0,'/')
        tree.delete('/n',15)
        self.assertTrue(tree.exist('/n'))

    def test_cambioDatos(self):
        tree = Ztree()
        tree.create('/n','contenido',False,True,0,'/')
        tree.setData('/n','DATOS')
        self.assertEqual(tree.getData('/n'),'DATOS')

    def test_comprobarHijos(self):
        tree = Ztree()
        tree.create('/n','padre',False,True,0,'/')
        tree.create('/n/nh1','un hijo',False,True,0,'/n')
        hijos = tree.tree.children('/n')
        nh1 = tree.tree.get_node('/n/nh1')
        self.assertIn(nh1, hijos)

if __name__ == '__main__':
    unittest.main()

