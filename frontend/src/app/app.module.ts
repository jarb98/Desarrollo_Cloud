import { routing } from "./app.routing";
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

import { AppComponent } from "./app.component";
import { LoginComponent } from "./login/login.component";
import { SigninComponent } from "./signin/signin.component";
import { EventosComponent } from './eventos/eventos.component';
import { EventosService } from './eventos/eventos.service';


@NgModule({
  declarations: [	AppComponent,
    LoginComponent,
    SigninComponent,
      EventosComponent
   ],
  imports: [BrowserModule, routing,FormsModule,
    ReactiveFormsModule,HttpClientModule],
  providers: [CookieService,EventosService],
  bootstrap: [AppComponent]
})
export class AppModule {}
