import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { User } from './user';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: "root"
})
/**El error viene de poner el constructor de las cookies acá
 * ,private cookies: CookieService
 *
 */
export class UsersService {
  constructor(private http: HttpClient,private cookies: CookieService) {}

  login(user: User): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/login/api', user);
  }

  signin(user: User): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/signin/api', user);
  }
  /**Guardar el token en las cookies*/
  setToken(token: string) {
    this.cookies.set("token", token);
  }

  /**Recuperar el token de las cookies*/
  getToken() {
    return this.cookies.get("token");
  }
  /**Para hacer logout */

  deleteToken(){
    this.cookies.delete("token");
  }

}
