public interface ReveilInterface extends Remote
{
    public void reveilMoi(int nbSecondes, CallbackInterface refObjet) throws RemoteExeption;   
}

// Pour endormir et reveiller (thread) ClientReveil, on utilise le moniteur d'un objet 'bidon'

public class ClientReveil{
    public static void main(String[] args) {
        ...
        ...
        ReveilInterface r = (ReveilInterface) Naming.lookup("http://"+IpServeur+" "+ port + "/Reveil");
        Object obj = new Object();
        Callback cb = new Callback(obj);

        r.reveilMoi(5, cb);
    }
}