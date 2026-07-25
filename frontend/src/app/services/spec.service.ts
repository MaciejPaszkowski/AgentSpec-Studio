import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { OptionsResponse, SpecCreateRequest, SpecResponse } from '../models/spec.model';

@Injectable({
  providedIn: 'root'
})
export class SpecService {
  private http = inject(HttpClient);
  private apiUrl = '/api/v1';

  getOptions(): Observable<OptionsResponse> {
    return this.http.get<OptionsResponse>(`${this.apiUrl}/options`);
  }

  createSpec(payload: SpecCreateRequest): Observable<SpecResponse> {
    return this.http.post<SpecResponse>(`${this.apiUrl}/specs`, payload);
  }

  getSpecs(): Observable<SpecResponse[]> {
    return this.http.get<SpecResponse[]>(`${this.apiUrl}/specs`);
  }

  getSpec(id: string): Observable<SpecResponse> {
    return this.http.get<SpecResponse>(`${this.apiUrl}/specs/${id}`);
  }

  deleteSpec(id: string): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.apiUrl}/specs/${id}`);
  }

  getExportZipUrl(id: string): string {
    return `${this.apiUrl}/specs/${id}/export/zip`;
  }
}
