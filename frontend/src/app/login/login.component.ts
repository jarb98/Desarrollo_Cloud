import { Component } from "@angular/core";
import { UsersService } from "../users/users.service";
import { Router } from '@angular/router';



@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})
export class LoginComponent {
  mail: string = "";
  contrasena: string = "";

  constructor(public userService: UsersService, private router: Router) {}

  login() {
    const user = {mail: this.mail, contrasena: this.contrasena};

    this.userService.login(user).subscribe(data => {
      /**Para poner antes de los metodos despues del login
       * const token = this.cookieService.get('access_token');
        const headers = new HttpHeaders().set('Authorization', 'Bearer ' + token);
        this.http.get('your api endpoint', { headers: headers });)
       */
      this.userService.setToken(data.token);
      const id_usuario = data.id_usuario;
      this.router.navigate(['/usuario/' + id_usuario + '/eventos'])
    });
    console.log(this.mail);
    console.log(this.contrasena);
  }
  signin_route(){
    this.router.navigate(['/signin']);
  }
}
