class B:
    def b(self):
     print('b from B')

class C:
  def b(self):
    print('c from C')

class D(B, C):
  def d(self):
    super(C, self).b()  
instance_d = D()
instance_d.d()