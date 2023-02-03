import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SigninComponent } from './signin/signin.component';
import { CookieService } from 'ngx-cookie-service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {
  title = 'frontend';


}
