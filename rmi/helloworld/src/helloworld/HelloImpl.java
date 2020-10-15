package helloworld;
import java.rmi.* ;
import java.rmi.server.* ;
public class HelloImpl extends UnicastRemoteObject implements HelloInterface 
{
	 private String message;
	 /* le constructeur */
	public HelloImpl (String s) throws RemoteException 
	{
		message = s;
		}
	/* implémentation de la méthode */
	public String sayHello () throws RemoteException
	{
		
	return message ;
	}
}