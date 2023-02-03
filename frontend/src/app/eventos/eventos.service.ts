import { Injectable } from "@angular/core";
import { HttpClient,HttpHeaders  } from "@angular/common/http";
import { Observable } from "rxjs";
import { Evento } from './evento';
import { UsersService } from '../users/users.service'



@Injectable()
export class EventosService {

constructor(private http: HttpClient,private usersService: UsersService) { }

public getListaEventos(id_usuario:number):Observable<Evento[]>
{
  const url = `http://127.0.0.1:5000/usuario/api/${id_usuario}/eventos`;
  /**
  const token = this.usersService.getToken();
  console.log(token)
  const httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'Bearer ' + token
    })
  };
*/

  /**Añadir  ,httpOptions*/
  return this.http.get<Evento[]>(url)

}


}
