<template>
  <main class="flex items-center justify-center p-4 min-h-screen">
    <div class="w-full max-w-2xl mx-auto">
      <HomeHeader />

      <EmailClassifierForm :is-loading="isLoading" @classify="handleClassificationRequest" />

      <ClassificationResult :is-loading="isLoading" :error="error" :result="result" />
    </div>
  </main>
</template>

<script setup lang="ts">
import { defineAsyncComponent, ref } from 'vue'
import axios from 'axios'
import LoadingSpinner from '@/components/base/LoadingSpinner.vue'
import HomeHeader from '@/components/emailClassification/HomeHeader.vue'
import type { EmailClassificationResult } from '@/@types/EmailClassificationResult'

const EmailClassifierForm = defineAsyncComponent({
  loader: () => import('@/components/emailClassification/EmailClassificationForm.vue'),
  loadingComponent: LoadingSpinner,
})

const ClassificationResult = defineAsyncComponent({
  loader: () => import('@/components/emailClassification/ClassificationResult.vue'),
  loadingComponent: LoadingSpinner,
})

const result = ref(null)
const isLoading = ref(false)
const error = ref<string | null>(null)

async function handleClassificationRequest(formData: EmailClassificationResult) {
  isLoading.value = true
  error.value = null
  result.value = null

  try {
    const response = await axios.post('http://localhost:8000/api/classify', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    result.value = response.data
  } catch (err) {
    console.error('Falha ao classificar o email:', err)
    error.value = 'Ocorreu um erro ao se comunicar com o servidor. Tente novamente.'
  } finally {
    isLoading.value = false
  }
}
</script>
