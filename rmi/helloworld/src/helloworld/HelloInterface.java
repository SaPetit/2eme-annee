package helloworld;

import java.rmi.* ;
public interface HelloInterface extends Remote 
{
/* méthode retournant un message prédéfini dans
l'objet appelé */
public String sayHello() throws RemoteException; 
}