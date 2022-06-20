from mpi4py import MPI

#=========================
# Objeto mensaje
#=========================
class Mensaje:
    def _init_(self, rank):
        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso " + str(rank)

#========================
# Programa principal 
#========================
if _name_ == "_main_":
    comm = MPI.COMM_WORLD 
    size = comm.Get_Size8()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank != 0 else size-1
    dst = rank-1 if rank != size-1 else 0 


    #========================
    # Envío no bloqueante 
    #========================
    comm.isend(s, dest = dst)

    #======================================
    # Recibir no bloqueante con espera
    # req: request (petición)
    #======================================
    req = comm.irecv(source = src)
    a = req.wait()

    print("Soy el proceso ", rank, ", el resultado es ", len(a, x), a.p)

